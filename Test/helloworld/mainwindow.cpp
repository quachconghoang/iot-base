#include "mainwindow.h"
#include "ui_mainwindow.h"

MainWindow::MainWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::MainWindow)
{
    ui->setupUi(this);
    setupDefault();
}

void MainWindow::setupDefault()
{
    ui->groupBox->setTitle("IP configs");
}

MainWindow::~MainWindow()
{
    delete ui;
}
