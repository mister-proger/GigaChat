#ifndef WIDGET_H
#define WIDGET_H

#include "authorizer.h"
#include "userinterface.h"
#include "utils/recentevent.h"
#include "utils/properties.h"

#include <QObject>

#include <QListWidget>
#include <QWidget>

#include <QStackedLayout>
#include <QListWidgetItem>
#include <QHBoxLayout>

class Widget : public QWidget
{
    Q_OBJECT

private:
    QStackedLayout* authorizeControl;
    Authorizer* helloScreen;
    UserInterface* UI;
    
    QListWidget* recentEvents;
    QList<RecentEvent*> eventsList;
    
    QWidget* eventsAndUI;
    QHBoxLayout* eventsAndUILayout;
    
    QString server_addres = "https://ru.gigachat.com";
    
    void initializeConnections();
    void constructEvents();
public:
    Widget(QWidget *parent = nullptr);
    ~Widget();
    
    void set_server_addres(const QString &newServer_addres);
    
public slots:
    void onAuthentication(QByteArray data);
    void addRecentEvents(QList<RecentEvent*> REList);

};
#endif // WIDGET_H
