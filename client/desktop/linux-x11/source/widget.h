#ifndef WIDGET_H
#define WIDGET_H

#include "authorizer.h"
#include "userinterface.h"
#include "utils/recentevent.h"

#include <QObject>

#include <QListView>
#include <QWidget>

#include <QStackedLayout>
#include <QHBoxLayout>

class Widget : public QWidget
{
    Q_OBJECT

private:
    QStackedLayout* AuthorizeControl;

    Authorizer* HelloScreen;
    
    UserInterface* UI;
    QListView* recentEvents;
    
    QWidget* EventsAndUI;
    QHBoxLayout* EventsAndUILayout;

    void InitializeConnections();
public:
    Widget(QWidget *parent = nullptr);
    ~Widget();


public slots:
    void OnAuthentication(bool success);

};
#endif // WIDGET_H
