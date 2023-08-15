#pragma once

#include <QObject>
#include <QAbstractButton>

//painting
#include <QPainterPath>
#include <QPaintEvent>
#include <QPainter>
#include <QRegion>
#include <QColor>
#include <QBrush>

class RecentEvent : public QAbstractButton
{
    Q_OBJECT
    
private:
    QPixmap ICON;
        
public:
    explicit RecentEvent(const QString& icon_path, 
                         const QString& tooltip, 
                         QWidget* parent = nullptr);

protected:
    void paintEvent(QPaintEvent* e) override;
};
