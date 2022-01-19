from PySide2 import QtWidgets

import config
from productor import Ui_MainWindow
import sys, db, shutil


class interfache(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()
        self.pImage.clicked.connect(self.choise_image_func)
        self.upd_btn.clicked.connect(self.cat_upd_func)
        self.add_category.clicked.connect(self.add_category_func)
        self.category_box.currentIndexChanged.connect(self.sub_upd_func)
        self.subcategory_box.currentIndexChanged.connect(self.prod_list_func)
        self.product_Box.currentIndexChanged.connect(self.card)
        self.add_product.clicked.connect(self.upload_prod)
        self.add_subcategory.clicked.connect(self.add_subcat_func)
        self.del_product.clicked.connect(self.bt_del_prod)
        self.del_cat.clicked.connect(self.bt_del_cat)
        self.del_subcat.clicked.connect(self.bt_delsubcat)


    ######FOTO ADD########
    def choise_image_func(self):
        filename = QtWidgets.QFileDialog.getOpenFileName(filter='*.jpg')
        self.image_place.setText(filename[0])



    #########UPD FUNCTIONS##########
    def cat_upd_func(self):
        self.category_box.clear()
        cat_out = []
        for cat in db.cats():
            cat_out.append(str(cat[0])+". "+str(cat[1]))
        self.category_box.addItems(cat_out)
    def sub_upd_func(self):
        sub_out = []
        self.subcategory_box.clear()
        for subs in db.sub_cats(self.category_box.currentText().split('. ')[0]):
            sub_out.append(str(subs[0])+'. '+str(subs[1]))
        self.subcategory_box.addItems(sub_out)
    def prod_list_func(self):
        self.product_Box.clear()
        prod_out = ['']
        for prod in db.prods(self.subcategory_box.currentText().split('. ')[0]):
            prod_out.append(str(prod[0])+'. '+str(prod[1]))
        self.product_Box.addItems(prod_out)



    def card(self):
        prod = db.get_product_card(self.product_Box.currentText().split('. ')[0])
        if prod is not None:
            self.select_id.setText(str(prod[0]))
            self.pName.setText(str(prod[2]))
            self.pDiscripton.setPlainText(str(prod[3]))
            self.image_place.setText(str(prod[4]))
            self.pCost.setText(str(prod[5]))
            self.pCount.setText(str(prod[6]))
            self.pByu.setText(str(prod[7]))
            self.pPlace.setText(str(prod[8]))
            self.pBar.setText(str(prod[9]))
            self.add_product.setText("Изменить товар")
        else:
            self.select_id.setText("Новый товар")
            self.pName.setText('')
            self.pDiscripton.setPlainText('')
            self.image_place.setText('')
            self.pCost.setText('')
            self.pCount.setText('')
            self.pByu.setText('')
            self.pPlace.setText('')
            self.pBar.setText('')
            self.add_product.setText("Добавить товар")



    ######### BUTONS ##########
    def add_category_func(self):
        text = self.category_name.text()
        if text != '':
            db.admin.add.category(text)
            self.cat_upd_func()
        else:
            pass
    def add_subcat_func(self):
        text = self.subcategory_name.text()
        print(text)
        if text != '':
            db.admin.add.sub_category(self.category_box.currentText().split('. ')[0], text)
            self.sub_upd_func()
        else:
            pass
    def upload_prod(self):
        if self.select_id.text() == "Новый товар":
            image = config.folder+"images/"+self.category_box.currentText().split('. ')[0]+'.'+self.subcategory_box.currentText().split('. ')[0]+'.'+self.pName.text().lower()+'.jpg'
            shutil.copyfile(self.image_place.text(),
                            image)
            db.admin.add.product(self.subcategory_box.currentText().split('. ')[0],
                                 self.pName.text(),
                                 self.pDiscripton.toPlainText(),
                                 image,
                                 self.pCost.text(),
                                 self.pCount.text(),
                                 self.pByu.text(),
                                 self.pPlace.text(),
                                 self.pBar.text()
                                 )
            self.prod_list_func()
    def bt_del_cat(self):
        id = self.category_box.currentText().split('. ')[0]
        db.admin.delete.category(id)
        self.cat_upd_func()

    def bt_delsubcat(self):
        id = self.subcategory_box.currentText().split('. ')[0]
        db.admin.delete.sub_category(id)
        self.cat_upd_func()

    def bt_del_prod(self):
        if self.select_id.text() != "Новый товар":
            db.admin.delete.product(self.select_id.text())
            self.cat_upd_func()
        else:
            pass



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    interfack = interfache()
    sys.exit(app.exec_())