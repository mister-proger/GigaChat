#pragma once

#include <QObject>
#include <QThread>

//utility classes
#include <QString>
#include <QStringView>
#include <QPixmap>

//widgets
#include <QWidget>
#include <QLabel>
#include <QLineEdit>
#include <QPushButton>
#include <QSvgWidget>

//layouts
#include <QHBoxLayout>
#include <QGridLayout>
#include <QSizePolicy>
#include <QResizeEvent>

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
        QLineEdit *Username,
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

public:
    explicit Authorizer(QWidget *parent = nullptr);

signals:
    void AuthenticationComplete(bool success);

public slots:
    void OnSubimtClicked();

};

