QT += core gui svgwidgets network

greaterThan(QT_MAJOR_VERSION, 4): QT += widgets

CONFIG += c++23

# You can make your code fail to compile if it uses deprecated APIs.
# In order to do so, uncomment the following line.
DEFINES += QT_DISABLE_DEPRECATED_BEFORE=0x060000    # disables all the APIs deprecated before Qt 6.0.0

SOURCES += \
    authorizer.cpp \
    main.cpp \
    mainwidgets/gridscrollingwidget.cpp \
    mainwidgets/scrollingwidget.cpp \
    mainwidgets/undefinedpage.cpp \
    userinterface.cpp \
    utils/nonewlineqlineedit.cpp \
    utils/properties.cpp \
    utils/recentevent.cpp \
    widget.cpp

HEADERS += \
    authorizer.h \
    mainwidgets/gridscrollingwidget.h \
    mainwidgets/scrollingwidget.h \
    mainwidgets/undefinedpage.h \
    stylesheets.h \
    userinterface.h \
    utils/nonewlineqlineedit.h \
    utils/properties.h \
    utils/recentevent.h \
    widget.h

# Default rules for deployment.
qnx: target.path = /tmp/$${TARGET}/bin
else: unix:!android: target.path = /opt/$${TARGET}/bin
!isEmpty(target.path): INSTALLS += target

TRANSLATIONS += \
	en_GB.qm

RESOURCES = assets/assets.qrc
