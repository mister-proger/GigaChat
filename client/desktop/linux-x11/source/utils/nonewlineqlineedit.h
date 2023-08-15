#pragma once

#include <QLineEdit>
#include <QKeyEvent>
#include <QObject>

class NoNewLineQLineEdit : public QLineEdit
{
    Q_OBJECT
public:
    NoNewLineQLineEdit(QWidget* parent);
    NoNewLineQLineEdit(const QString &str, QWidget* parent = nullptr);
    ~NoNewLineQLineEdit();
    
protected:
    void keyPressEvent(QKeyEvent *e) override;
    
signals:
    void EnterPressed();
};

