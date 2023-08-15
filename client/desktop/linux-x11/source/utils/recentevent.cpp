#include "recentevent.h"

RecentEvent::RecentEvent(const QString &icon_path, 
                         const QString &tooltip, 
                         QWidget *parent) 
    : QAbstractButton{parent}
{
    setCheckable(false);
    setToolTip(tooltip);
    ICON = QPixmap(icon_path);
    
}

void RecentEvent::paintEvent(QPaintEvent *e)
{
    QRect r = e->rect();
    QPainter painter(this);
    
    QPainterPath circleBig, circleSmall;
    circleBig.addEllipse(r);
    circleSmall.addEllipse(QRect(r.left()+5, r.top()+5, r.width()-5, r.width()-5));
    
    painter.fillPath(circleBig, Qt::red);
    
    painter.setClipPath(circleSmall);
    painter.drawPixmap(r, ICON);
    
}
