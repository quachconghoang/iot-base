#include <QApplication>
#include <QLabel>
#include <QWidget>

#include "mainwindow.h"

#include "opencv2/opencv.hpp"

int main(int argc, char *argv[ ])
{
//	QApplication app(argc, argv);
//	QLabel hello("<center>Welcome to my first Qt program</center>");
//	hello.setWindowTitle("My First Qt Program");
//	hello.resize(400, 400);
//	hello.show();
//	return app.exec();
    QApplication a(argc, argv);
    MainWindow w;
    w.show();

    return a.exec();

}