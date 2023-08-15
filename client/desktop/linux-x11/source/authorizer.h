#pragma once

#include <QObject>

//utility classes
#include <QStringView>
#include <QString>
#include <QPixmap>

//widgets
#include <QPushButton>
#include <QSvgWidget>
#include <QLineEdit>
#include "nonewlineqlineedit.h"
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
        void CreateWidgets(QWidget* parent);
        void SetupLayout();
        void InitializeConnections(QWidget* parent);
        explicit InputField(QWidget* parent = nullptr);
        ~InputField();
    
        void Reposition(QRect parentGeometry);
        bool ParseAuthentication();
    
        QWidget *Widget;
        QGridLayout *Layout;
        //QSizePolicy Alignment;
        NoNewLineQLineEdit *Username,
                           *Password,
                           *Captcha;
        QSvgWidget* SubmitBG;
        QPushButton *Submit,
                    *ChangeCaptcha;
        QLabel *__SOMETHING__; //that window on the side
    };
    
    InputField* Field;
    QHBoxLayout* ThisLayout;
    const QString BGImagePath = ":/resources/AuthorizeBG.svg";
    //QLabel* BackgroundImage;
    static const int resizeFactorH = 2,
                     resizeFactorV = 2;

protected:
    void resizeEvent(QResizeEvent* e) override;
    //void keyPressEvent(QKeyEvent *event) override;

public:
    explicit Authorizer(QWidget *parent = nullptr);

signals:
    void AuthenticationComplete(bool success);

public slots:
    void OnSubimtClicked();

};

