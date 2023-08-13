#include "authorizer.h"

void Authorizer::InputField::CreateWidgets(QWidget* parent)
{
    qDebug() << __PRETTY_FUNCTION__;

    Widget = new QWidget(parent);
    QSize parentSize = parent->size();
    Widget->resize(parentSize.width()/resizeFactorH,
                   parentSize.height()/resizeFactorV);

    Layout = new QGridLayout(Widget);
    Username = new QLineEdit(tr("Username goes here,"));
    Password = new QLineEdit(tr("Password - here..."));
    Captcha  = new QLineEdit(tr("...and Captcha - here."));
    ChangeCaptcha = new QPushButton(tr("Change\ncaptcha"));
    
    SubmitBG = new QSvgWidget(":/resources/LoginBN.svg");
    Submit = new QPushButton(tr("Log in"), SubmitBG);
    Submit->setStyleSheet("background-color: transparent; border: none; color: red;");
    Submit->setGeometry(SubmitBG->geometry());
    //Submit->setSizePolicy(QSizePolicy::Expanding, QSizePolicy::Expanding);
    //QHBoxLayout *SubmitBGLayout = new QHBoxLayout(SubmitBG); //IS MANAGED BY IT'S PARENT, NO MEMORY LEAKS
    //SubmitBGLayout->addWidget(Submit);
    
    __SOMETHING__ = new QLabel(tr("Log iv via qr-code"));
    __SOMETHING__->setAutoFillBackground(true);
}
void Authorizer::InputField::SetupLayout()
{
    qDebug() << __PRETTY_FUNCTION__;

    Layout->addWidget(Username,      0, 0, 1, 4);
    Layout->addWidget(Password,      1, 0, 1, 4);
    Layout->addWidget(Captcha,       2, 0, 1, 3);
    Layout->addWidget(ChangeCaptcha, 2, 3, 1, 1);
    Layout->addWidget(SubmitBG,      3, 0, 1, 4); //Since SubmitBG is parent of Submit, it is added automatically
    Layout->addWidget(__SOMETHING__, 0, 4, 4, 3);
    for(int i = 0; i < Layout->count(); ++i)
    {
        //All widgets must take as much space as they can";
        Layout->itemAt(i)->widget()->setSizePolicy(QSizePolicy::Expanding, QSizePolicy::Expanding);
        qDebug().quote() << Layout->itemAt(i)->widget()->objectName();

    }
}
void Authorizer::InputField::InitializeConnections(QWidget* parent)
{
    qDebug() << __PRETTY_FUNCTION__;
    connect(Submit, SIGNAL(clicked()),
            parent, SLOT(OnSubimtClicked()),
            Qt::DirectConnection);
}
Authorizer::InputField::InputField(QWidget* parent)
{
    // ORDER IS CRUCIAL
    CreateWidgets(parent);
    SetupLayout();
    InitializeConnections(parent);
}

Authorizer::InputField::~InputField()
{
    delete Widget;
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

//TODO: REIMPLEMENT
bool Authorizer::InputField::ParseAuthentication()
{
    return (Username->text() == "test" && Password->text() == "1234");
}

Authorizer::Authorizer(QWidget *parent) : QSvgWidget{parent}
{
#ifdef QT_DEBUG
    setStyleSheet("border: 5px solid red");
#endif
    setMinimumSize(666, 400);
    load(BGImagePath);
    Field = new InputField(this);
    Field->Reposition(geometry()); //this->geometry()

}

void Authorizer::OnSubimtClicked()
{
    qDebug() << __PRETTY_FUNCTION__;
    emit AuthenticationComplete(Field->ParseAuthentication());

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
