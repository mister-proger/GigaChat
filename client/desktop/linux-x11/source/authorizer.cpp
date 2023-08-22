#include "authorizer.h"

void Authorizer::InputField::createWidgets()
{
    widget = new QWidget(parent);
    layout   = new QGridLayout(widget);
    username = new NoNewLineQLineEdit(tr("Username goes here,"));
    password = new NoNewLineQLineEdit(tr("Password - here..."));
    captcha  = new NoNewLineQLineEdit(tr("...and Captcha - here."));
    changeCaptcha = new QPushButton(tr("Change\ncaptcha"));
    submitBG = new QSvgWidget(":/resources/LoginBN.svg");
    submit = new QPushButton(tr("Log in"), submitBG);
    QRLogin = new QLabel(tr("Log in via qr-code\n(temporary unavailable)"));    
    
    QHBoxLayout* submitLayout = new QHBoxLayout(submitBG);
    submitLayout->setContentsMargins(0, 0, 0, 0);
    submitLayout->addWidget(submit);
    submit->setSizePolicy(QSizePolicy::Expanding, QSizePolicy::Expanding);  
    QRLogin->setAutoFillBackground(true);
    QRLogin->setAlignment(Qt::AlignCenter);
}
void Authorizer::InputField::setupLayout()
{
    layout->addWidget(username,      0, 0, 1, 4);
    layout->addWidget(password,      1, 0, 1, 4);
    layout->addWidget(captcha,       2, 0, 1, 3);
    layout->addWidget(changeCaptcha, 2, 3, 1, 1);
    layout->addWidget(submitBG,      3, 0, 1, 4);
    layout->addWidget(QRLogin,       0, 4, 4, 3);
    
    for(int i = 0; i < layout->columnCount(); ++i)
    for(int j = 0; j < layout->rowCount(); ++j)
    {
        layout->setColumnStretch(i, 1);
        layout->setRowStretch(j, 1);
    }
    
    for(int i = 0; i < layout->count(); ++i)
        layout->itemAt(i)->widget()->setSizePolicy(
                    QSizePolicy::Expanding, 
                    QSizePolicy::Expanding);
}
void Authorizer::InputField::initializeConnections()
{
    connect(submit  , SIGNAL(clicked())     , parent   , SLOT(sendLoginRequest()), Qt::DirectConnection);
    connect(captcha , SIGNAL(enterPressed()), parent   , SLOT(sendLoginRequest()), Qt::DirectConnection);
    connect(username, SIGNAL(enterPressed()), password , SLOT(setFocus())        , Qt::DirectConnection);
    connect(password, SIGNAL(enterPressed()), captcha  , SLOT(setFocus())        , Qt::DirectConnection);
}
void Authorizer::InputField::setStyles()
{
    submitBG->setStyleSheet(StyleSheets::SVGBGSS);
}
Authorizer::InputField::InputField(QWidget* newParent)
    : parent{newParent}
{
    createWidgets();
    setupLayout();
    initializeConnections();
    setStyles();
    reposition(newParent->geometry());
}
void Authorizer::InputField::reposition(QRect parentGeometry)
{
    int x1 = parentGeometry.height(),
        y1 = parentGeometry.width();
    int x2 = x1/resizeFactorV,
        y2 = y1/resizeFactorH;

    widget->setGeometry( (y1-y2)/2, (x1-x2)/2, y2, x2 );
}
Authorizer::InputField::~InputField()
{
    delete widget;
}


Authorizer::Authorizer(QString server, QWidget *parent) 
    : QSvgWidget{parent}, server_address{server} 
{
    setMinimumSize(666, 420);
    load(BGImagePath);
    
    field = new InputField(this);
    welcomeBack = new QLabel(tr("Welcome back!"), this);
    welcomeBack->setStyleSheet(StyleSheets::LabelSS);
    welcomeBack->setMargin(30);
    
    connect(&mgr, &QNetworkAccessManager::finished, 
            this, &Authorizer::parseResponse,
            Qt::DirectConnection);
}

void Authorizer::sendLoginRequest()
{
    
    if (field->password->isDefault() || field->username->isDefault())
    {
        failedAuth(tr("Error: username and password can't be empty"));
        return;
    }
    
    QString requestUrl = 
            QString("%1/auth?login=%2&password=%3%4")
            .arg(server_address)
            .arg(field->username->text())
            .arg(field->password->text())
            .arg("");
    
    QNetworkRequest authRequest = QNetworkRequest(QUrl(requestUrl));
    mgr.get(authRequest);
}
void Authorizer::parseResponse(QNetworkReply* response)
{
    DEBUG( "DATA RECIEVED:\n\e[1;33;40m" << response->readAll() << "\e[0m" );
    
    bool success;
    
    if(response->error() != QNetworkReply::NoError)
    {
        DEBUG( "\e[1;33;40mNETWORK ERROR RECIEVED:" 
                 << response->error() 
                 << "\e[0m" );
        QString error = tr("Login request failed:\n"
                           "Error code: %1\n%2");
        failedAuth(error.arg(QString::number(response->error()))
                        .arg(response->errorString()));
#ifndef QT_DEBUG
        return;
#endif
    }
    
    success = field->username->text() == "test"; //TODO: IMPLEMENT CHECK
    
    if (success) emit successfullyAuthorized(response->readAll());
    else {
#ifndef QT_DEBUG
        failedAuth(tr("Login incorrect"))
#endif
                ; }
}
void Authorizer::failedAuth(QString context)
{
    if (field->errorMsg != nullptr) goto textset;
    {
        setStyleSheet(StyleSheets::FailedAuthSS);
        QLabel* temp = new QLabel();
        temp->setWordWrap(true);
        temp->setSizePolicy(QSizePolicy::Expanding, QSizePolicy::Expanding);
        temp->setAlignment(Qt::AlignLeft | Qt::AlignVCenter);
        temp->setStyleSheet("color: red; font: bold 12pt");
        field->layout->addWidget(temp, 4, 0, 1, 7);
        field->errorMsg = temp; //i'm lazy 
    }

textset:
    field->errorMsg->setText(context);
    
}

void Authorizer::set_server_address(const QString &newServer_address)
{
    server_address = newServer_address;
}
void Authorizer::resizeEvent(QResizeEvent *e)
{
    QSvgWidget::resizeEvent(e);
    field->reposition(geometry()); 
}
