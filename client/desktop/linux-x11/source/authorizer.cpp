#include "authorizer.h"

void Authorizer::InputField::createWidgets()
{
    widget = new QWidget(parent);
    QSize parentSize = parent->size();
    widget->resize(parentSize.width()/resizeFactorH,
                   parentSize.height()/resizeFactorV);

    layout   = new QGridLayout(widget);
    username = new NoNewLineQLineEdit(tr("Username goes here,"));
    password = new NoNewLineQLineEdit(tr("Password - here..."));
    captcha  = new NoNewLineQLineEdit(tr("...and Captcha - here."));
    changeCaptcha = new QPushButton(tr("Change\ncaptcha"));
    
    submitBG = new QSvgWidget(":/resources/LoginBN.svg");
    QHBoxLayout* submitLayout = new QHBoxLayout(submitBG);
    submitLayout->setContentsMargins(0, 0, 0, 0);
    submit = new QPushButton(tr("Log in"), submitBG);
    submitLayout->addWidget(submit);
    submit->setSizePolicy(QSizePolicy::Expanding, QSizePolicy::Expanding);  
    submitBG->setStyleSheet("background-color: transparent;"
                            "border: 4px solid white;"
                            "border-radius: 5px;"
                            "color: white;"
                            "font-size: 24pt");
    QRLogin = new QLabel(tr("Log in via qr-code\n(temporary unavailable)"));
    QRLogin->setAutoFillBackground(true);
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
    submit->setStyleSheet("color: white;"
                          "font-size: 14pt"
                          "border: 2px solid white"
                          "border-radius: 5px");
}
Authorizer::InputField::InputField(QWidget* newParent)
    : parent{newParent}
{
    createWidgets();
    setupLayout();
    initializeConnections();
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
#ifdef QT_DEBUG
    setStyleSheet("border: 5px solid red");
    qDebug() << server_address; 
#endif
    
    //setMinimumSize(1366, 768); //TODO: change size    
    setMinimumSize(666, 420);
    load(BGImagePath);
    field = new InputField(this);
    field->reposition(geometry());
    
    connect(&mgr, &QNetworkAccessManager::finished, 
            this, &Authorizer::parseResponse,
            Qt::DirectConnection);
}

void Authorizer::sendLoginRequest()
{
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
                           "Error code: ");
        failedAuth(error + QString::number(response->error()));
#ifndef QT_DEBUG
        return;
#endif
    }
    
    success = field->username->text() == "test"; //TODO: IMPLEMENT CHECK
    
    if (success) emit successfullyAuthorized(response->readAll());
    else failedAuth(tr("Login incorrect"));
}

//TODO : FIX
void Authorizer::failedAuth(QString context)
{
    setStyleSheet("NoNewLineQLineEdit {"
                  "border: 4px solid red;"
                  "border-radius: 2px;"
                  "background-color: #f0f0f0;"
                  "}");
    QLabel* errorMsg = new QLabel(context, this);
    errorMsg->setSizePolicy(QSizePolicy::Expanding, QSizePolicy::Expanding);
    field->layout->addWidget(errorMsg, 4, 0, 1, 7);
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
