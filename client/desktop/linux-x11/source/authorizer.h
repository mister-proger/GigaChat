#pragma once

#include <QObject>

//stdc++
#include <optional>
#ifdef QT_DEBUG
    #include <iostream>
    #define DEBUG(str) qDebug() << str
#else
    #define DEBUG(str) 
#endif

#include <QStringView>
#include <QByteArray>
#include <QString>
#include <QPixmap>
#include <QDebug>

#include <QPushButton>
#include <QSvgWidget>
#include <QLineEdit>
#include "utils/nonewlineqlineedit.h"
#include <QWidget>
#include <QLabel>

#include <QHBoxLayout>
#include <QGridLayout>
#include <QSizePolicy>

#include <QResizeEvent>
#include <QKeyEvent>

#include <QNetworkAccessManager>
#include <QNetworkRequest>
#include <QNetworkReply>
#include <QUrl>

#include "stylesheets.h"

class Authorizer : public QSvgWidget
{
    Q_OBJECT

private:

    struct InputField
    {
        QWidget* parent; 
        
        void createWidgets();
        void setupLayout();
        void initializeConnections();
        void setStyles();
        explicit InputField(QWidget* newParent = nullptr);
        ~InputField();
    
        void reposition(QRect parentGeometry);
    
        QWidget *widget;
        QGridLayout *layout;
        NoNewLineQLineEdit *username,
                           *password,
                           *captcha;
        QSvgWidget  *submitBG;
        QPushButton *submit,
                    *changeCaptcha;
        QLabel *QRLogin;
        
        QLabel* errorMsg = nullptr;
    };
    
    QNetworkAccessManager mgr;
    
    QLabel* welcomeBack;
    
    InputField* field;
    QHBoxLayout* thisLayout;
    const QString BGImagePath = ":/resources/AuthorizeBG.svg";
    static const int resizeFactorH = 2,
                     resizeFactorV = 2;
    
    QString server_address;

protected:  
    void resizeEvent(QResizeEvent* e) override;

public:
    explicit Authorizer(QString server, QWidget* parent = nullptr);
    
    void set_server_address(const QString &newServer_address);
    
signals:
    void successfullyAuthorized(QByteArray response);
    
public slots:
    void parseResponse(QNetworkReply* response);
    void failedAuth(QString context);
    void sendLoginRequest();
};
