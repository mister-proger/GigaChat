#include "authorizer.h"

void Authorizer::InputField::CreateWidgets()
{
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
    Layout->addWidget(Username,      0, 0, 1, 4);
    Layout->addWidget(Password,      1, 0, 1, 4);
    Layout->addWidget(Captcha,       2, 0, 1, 3);
    Layout->addWidget(ChangeCaptcha, 2, 3, 1, 1);
    Layout->addWidget(SubmitBG,      3, 0, 1, 4);
    Layout->addWidget(QRLogin, 0, 4, 4, 3);
    for(int i = 0; i < Layout->count(); ++i)
        Layout->itemAt(i)->widget()->setSizePolicy(
                    QSizePolicy::Expanding, 
                    QSizePolicy::Expanding);
    
}
void Authorizer::InputField::InitializeConnections()
{
    connect(Submit  , SIGNAL(clicked())     , parent   , SLOT(sendLoginRequest()), Qt::DirectConnection);
    connect(Captcha , SIGNAL(EnterPressed()), parent   , SLOT(sendLoginRequest()), Qt::DirectConnection);
    connect(Username, SIGNAL(EnterPressed()), Password , SLOT(setFocus())        , Qt::DirectConnection);
    connect(Password, SIGNAL(EnterPressed()), Captcha  , SLOT(setFocus())        , Qt::DirectConnection);
}
Authorizer::InputField::InputField(QWidget* newParent)
    : parent{newParent}
{
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
}

Authorizer::InputField::~InputField()
{
    delete Widget;
}


Authorizer::Authorizer(QString server, QWidget *parent) 
    : QSvgWidget{parent}, server_address{server} 
{
#ifdef QT_DEBUG
    setStyleSheet("border: 5px solid red");
#endif
    
    setMinimumSize(1366, 768); //TODO: change size 
    load(BGImagePath);
    Field = new InputField(this);
    Field->Reposition(geometry());
    
    connect(&mgr, &QNetworkAccessManager::finished, 
            this, &Authorizer::ParseResponse,
            Qt::DirectConnection);
    
}

void Authorizer::sendLoginRequest()
{
    QString requestUrl = 
            QString("%1/auth?login=%2&password=%3%4")
            .arg(server_address)
            .arg(Field->Username->text())
            .arg(Field->Password->text())
            .arg("");
    
    QNetworkRequest authRequest = QNetworkRequest(QUrl(requestUrl));
    mgr.get(authRequest);
}
void Authorizer::ParseResponse(QNetworkReply* response)
{
    DEBUG( "DATA RECIEVED:\n\e[1;33;40m" << response->readAll() << "\e[0m" );
    
    bool success;
    
    if(response->error() != QNetworkReply::NoError)
    {
        DEBUG( "\e[1;33;40mNETWORK ERROR RECIEVED:" 
                 << response->error() 
                 << "\e[0m" );
        QString error = tr("Login request failed:\n"
                           "Error code: ");
        failedAuth(error + QString::number(response->error()));
#ifndef QT_DEBUG
        return;
#endif
    }
    
    success = Field->Username->text() == "test"; //TODO: IMPLEMENT CHECK
    
    if (success) emit successfullyAuthorized(response->readAll());
    else failedAuth(tr("Login incorrect"));
}

//TODO : Implement
void Authorizer::failedAuth(QString context)
{
    const QString errorSheet = "border: 1px red;";
    Field->Username->setStyleSheet(errorSheet);
    Field->Password->setStyleSheet(errorSheet);
    QLabel* errorMsg = new QLabel(context, this);
    errorMsg->setSizePolicy(QSizePolicy::Expanding, QSizePolicy::Expanding);
    Field->Layout->addWidget(errorMsg, 4, 0, 1, 7);
}

void Authorizer::set_server_address(const QString &newServer_address)
{
    server_address = newServer_address;
}
void Authorizer::resizeEvent(QResizeEvent *e)
{
    QSvgWidget::resizeEvent(e);
    Field->Reposition(geometry()); 
}
