pic_1, pic_2, pic_3, pic_4, pic_5, pic_6 = 1, 2, 3, 4, 5, 6

array = list()

[array.append(pic_"i")]


        pictures = [os.path.join(upload_dir, picture)
                    for picture in os.listdir('upload')]
                    
        picture_frames = [self.layout_gallery.itemAtPosition(r, c) for r in range(
            self.layout_gallery.rowCount()) for c in range(self.layout_gallery.columnCount())]

        [self.layout_gallery.removeWidget(pic) for pic in picture_frames]

        print(picture_frames)

        # self.pic_1.setIcon(QIcon(pictures[1]))
        # print(type(self.pic_1), picture_frames[0])
        # count = 0
        # for picture in picture_frames:
        #     picture.setIcon(QIcon(pictures[count]))
        #     count += 1