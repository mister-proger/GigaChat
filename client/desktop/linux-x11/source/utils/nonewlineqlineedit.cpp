#include "nonewlineqlineedit.h"

NoNewLineQLineEdit::NoNewLineQLineEdit(QWidget* parent) 
    : QLineEdit{parent} {}
NoNewLineQLineEdit::NoNewLineQLineEdit(const QString &str, QWidget* parent) 
    : QLineEdit(str, parent) {}
NoNewLineQLineEdit::~NoNewLineQLineEdit(){}

void NoNewLineQLineEdit::keyPressEvent(QKeyEvent *e)
{
    if(e->key() == Qt::Key_Enter || e->key() == Qt::Key_Return) emit EnterPressed();
    else QLineEdit::keyPressEvent(e);
} 
