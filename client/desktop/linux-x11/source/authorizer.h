#pragma once

#include <QObject>

//stdc++
#include <optional>
#ifdef QT_DEBUG
    #include <iostream>
#endif

//utility classes
#include <QStringView>
#include <QByteArray>
#include <QString>
#include <QPixmap>

//widgets
#include <QPushButton>
#include <QSvgWidget>
#include <QLineEdit>
#include "utils/nonewlineqlineedit.h"
#include <QWidget>
#include <QLabel>

//layouts
#include <QHBoxLayout>
#include <QGridLayout>
#include <QSizePolicy>

//events
#include <QResizeEvent>
#include <QKeyEvent>

//network
#include <QNetworkAccessManager>
#include <QNetworkRequest>
#include <QNetworkReply>
#include <QUrl>


class Authorizer : public QSvgWidget
{
    Q_OBJECT

private:

    struct InputField
    {
        QWidget* parent; //stores authorizer's parent
        
        void CreateWidgets();
        void SetupLayout();
        void InitializeConnections();
        explicit InputField(QWidget* newParent = nullptr);
        ~InputField();
    
        void Reposition(QRect parentGeometry);
    
        QWidget *Widget;
        QGridLayout *Layout;
        //QSizePolicy Alignment;
        NoNewLineQLineEdit *Username,
                           *Password,
                           *Captcha;
        QSvgWidget* SubmitBG;
        QPushButton *Submit,
                    *ChangeCaptcha;
        QLabel *QRLogin; //that window on the side
    };
    
    QNetworkAccessManager mgr;
    
    
    InputField* Field;
    QHBoxLayout* ThisLayout;
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
    //void OnSubimtClicked();
    void ParseResponse(QNetworkReply* response);
    void failedAuth(QString context);
    void sendLoginRequest();
};

