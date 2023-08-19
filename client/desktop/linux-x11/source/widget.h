#ifndef WIDGET_H
#define WIDGET_H

#include "authorizer.h"
#include "userinterface.h"
#include "utils/recentevent.h"
#include "utils/properties.h"

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
    
    QString server_addres = "https://ru.gigachat.com";
    
public:
    Widget(QWidget *parent = nullptr);
    ~Widget();

    
    void set_server_addres(const QString &newServer_addres);
    
public slots:
    void OnAuthentication(QByteArray data);

};
#endif // WIDGET_H
