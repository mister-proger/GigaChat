#ifndef WIDGET_H
#define WIDGET_H

#include "authorizer.h"

#include <QObject>
#include <QWidget>
#include <QStackedLayout>
#include <QTabWidget>

class Widget : public QWidget
{
    Q_OBJECT

private:

    enum struct ScreenType
    {
        AuthorizeScreen = 0,
        ApplicationScreen = 1
    };
    QStackedLayout* AuthorizeControl;

    Authorizer* HelloScreen;
    QPushButton* temporar = new QPushButton("HAHAHAH"); // // // // // // //

    void InitializeConnections();
public:
    Widget(QWidget *parent = nullptr);
    ~Widget();


public slots:
    void OnAuthentication(bool success);

};
#endif // WIDGET_H
