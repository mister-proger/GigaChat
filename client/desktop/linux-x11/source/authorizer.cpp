#include "authorizer.h"

void Authorizer::InputField::CreateWidgets()
{
    qDebug() << __PRETTY_FUNCTION__;

    Widget = new QWidget(parent);
    QSize parentSize = parent->size();
    Widget->resize(parentSize.width()/resizeFactorH,
                   parentSize.height()/resizeFactorV);

    Layout = new QGridLayout(Widget);
    Username = new NoNewLineQLineEdit(tr("Username goes here,"));
    Password = new NoNewLineQLineEdit(tr("Password - here..."));
    Captcha  = new NoNewLineQLineEdit(tr("...and Captcha - here."));
    ChangeCaptcha = new QPushButton(tr("Change\ncaptcha"));
    
    SubmitBG = new QSvgWidget(":/resources/LoginBN.svg");
    Submit = new QPushButton(tr("Log in"), SubmitBG);
    Submit->setStyleSheet("background-color: transparent; border: none; color: black;");
    Submit->setGeometry(SubmitBG->geometry());
    
    QRLogin = new QLabel(tr("Log in via qr-code\n(temporary unavailable)"));
    QRLogin->setAutoFillBackground(true);
}
void Authorizer::InputField::SetupLayout()
{
    qDebug() << __PRETTY_FUNCTION__;

    Layout->addWidget(Username,      0, 0, 1, 4);
    Layout->addWidget(Password,      1, 0, 1, 4);
    Layout->addWidget(Captcha,       2, 0, 1, 3);
    Layout->addWidget(ChangeCaptcha, 2, 3, 1, 1);
    Layout->addWidget(SubmitBG,      3, 0, 1, 4); //Since SubmitBG is parent of Submit, it is added automatically
    Layout->addWidget(QRLogin, 0, 4, 4, 3);
    for(int i = 0; i < Layout->count(); ++i)
    {
        //All widgets must take as much space as they can";
        Layout->itemAt(i)->widget()->setSizePolicy(QSizePolicy::Expanding, QSizePolicy::Expanding);
        qDebug().quote() << Layout->itemAt(i)->widget()->objectName();
    
    }
    
}
void Authorizer::InputField::InitializeConnections()
{
    qDebug() << __PRETTY_FUNCTION__;
    qDebug().quote() << "\e[96m" << parent /*<< "\e[0m"*/;
    qDebug().quote() << "DA PARENT \e[0m";
    
    connect(Submit  , SIGNAL(clicked())     , parent   , SLOT(sendLoginRequest()), Qt::DirectConnection);
    connect(Captcha , SIGNAL(EnterPressed()), parent   , SLOT(sendLoginRequest()), Qt::DirectConnection);
    connect(Username, SIGNAL(EnterPressed()), Password , SLOT(setFocus())        , Qt::DirectConnection);
    connect(Password, SIGNAL(EnterPressed()), Captcha  , SLOT(setFocus())        , Qt::DirectConnection);
}
Authorizer::InputField::InputField(QWidget* newParent)
    : parent{newParent}
{
    // ORDER IS CRUCIAL
    CreateWidgets();
    SetupLayout();
    InitializeConnections();
}

void Authorizer::InputField::Reposition(QRect parentGeometry)
{
    int x1 = parentGeometry.height(),
        y1 = parentGeometry.width();

    int x2 = x1/resizeFactorV,
        y2 = y1/resizeFactorH;

    Widget->setGeometry( (y1-y2)/2, (x1-x2)/2, y2, x2 );
    
    qDebug() << parentGeometry << Widget->geometry() << ' ' << x1 << ' ' << x2 << ' ' << y1 << ' ' << ' ' << y2;
    
}

Authorizer::InputField::~InputField()
{
    delete Widget;
}


Authorizer::Authorizer(QString server, QWidget *parent) 
    : QSvgWidget{parent}, server_address{server} 
{
#ifdef QT_DEBUG
    if(parent == nullptr)
    {
        std::cerr << "nullptr passed to authorizer";
        std::terminate();
    }
    qDebug() << this->parent();
    qDebug() << "THE PARENT";
    setStyleSheet("border: 5px solid red");
#endif
    
    setMinimumSize(1366, 768); // make minimum size different, this one is way too big
    load(BGImagePath);
    Field = new InputField(this);
    Field->Reposition(geometry());
    
    connect(&mgr, &QNetworkAccessManager::finished, 
            this, &Authorizer::ParseResponse,
            Qt::DirectConnection);
    
}

void Authorizer::sendLoginRequest()
{
    qDebug() << __PRETTY_FUNCTION__;
    bool hasAccount = true; //TODO: IMPLEMENT
    QString requestUrl = 
            QString("%1/%2?login=%3&password=%4%5")
            .arg(server_address)
            .arg(hasAccount ? "auth" : "register")
            .arg(Field->Username->text())
            .arg(Field->Password->text())
            .arg(""); //additional info
    
    QNetworkRequest authRequest(QUrl(requestUrl));
    mgr.get(authRequest);
}
void Authorizer::ParseResponse(QNetworkReply* response)
{
    qDebug() << "DATA RECIEVED:\n\e[1;33;40m" << response->readAll() << "\e[0m";
    
    if(response->error() != QNetworkReply::NoError)
    {
        qDebug() << "\e[1;33;40mNETWORK ERROR RECIEVED:" 
                 << response->error() 
                 << "\e[0m";
        QString error = tr("Login request failed:\n"
                           "Error code: ");
        failedAuth(error + QString::number(response->error()));
    }
    
    bool success = true;
    if (success) emit successfullyAuthorized(response->readAll());
    else failedAuth(tr("Login incorrect"));
}

//TODO : Implement
void Authorizer::failedAuth(QString context)
{
    qDebug() << "failedAuth called";
}

void Authorizer::set_server_address(const QString &newServer_address)
{
    server_address = newServer_address;
}

void Authorizer::resizeEvent(QResizeEvent *e)
{
    //fucking bullshit
    /*
    QSize newSize = e->size();
    int AspectRatio = (newSize.width() * 36768) / newSize.height();
    if (AspectRatio < 36768)
        newSize = QSize(newSize.width(), newSize.width());
    else if (AspectRatio > 36768*2) 
        newSize = QSize(newSize.height()*2, newSize.height());
    
    qDebug() << newSize;
    QSvgWidget::resizeEvent(new QResizeEvent(newSize, e->oldSize()));
    */
    QSvgWidget::resizeEvent(e);
    qDebug() << "\e[31mresize event triggered\e[0m";
    Field->Reposition(geometry()); //this->geometry()
}
