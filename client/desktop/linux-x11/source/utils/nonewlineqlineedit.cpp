#include "nonewlineqlineedit.h"

NoNewLineQLineEdit::NoNewLineQLineEdit(QWidget* parent) 
    : QLineEdit{parent} {}
NoNewLineQLineEdit::NoNewLineQLineEdit(const QString &str, QWidget* parent) 
    : QLineEdit(str, parent), defaultText{str} {}
NoNewLineQLineEdit::~NoNewLineQLineEdit(){}

void NoNewLineQLineEdit::keyPressEvent(QKeyEvent *e)
{
    if(e->key() == Qt::Key_Enter || e->key() == Qt::Key_Return) 
    {
        emit EnterPressed();
        return;
    }
    
    if (text() == defaultText) 
    {
        setText("");
        setStyleSheet(changedStyleSheet);
    }
    QLineEdit::keyPressEvent(e);
    if (text().isEmpty()) 
    {
        setStyleSheet(defaultStyleSheet);
        setText(defaultText);
    }
} 
