from scaning_path_save_path import scan_yandex, yandex_upload, scan_dir, proxy_parse
from threading import Timer
import yadisk


id = "225715a2b5c54bd1869461334e486091"
pas = "24ae9c3e085b4f4cb876cd7bb1721eac"
token = "AgAAAAAcXZXeAAXkHd0nDq7LAEGPoc61Lmrg2wY"

ya = yadisk.YaDisk(id, pas, token)


lst_1 = scan_yandex(id, pas, token)
lst_2 = scan_dir("/home/zico/PycharmProjects/untitled/photo/")


arg_list = [id, pas, token, lst_2, lst_1]
t = Timer(10.0, yandex_upload, arg_list)
p = Timer(10.0, proxy_parse)
t.start()
p.start()

