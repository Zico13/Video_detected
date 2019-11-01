from imageai.Detection import VideoObjectDetection
from proxy_scan import proxy_api
import os
import cv2
from datetime import datetime
import telebot


def proxy():
    with open('/home/zico/PycharmProjects/untitled/proxy/proxy.txt', 'r') as inf:
        for line in inf:
            return line


execution_path = os.getcwd()
artur_id = "239289123"
sofi_id = "870800205"
telebot.apihelper.proxy = {'https': "{}".format(str(proxy_api()))}
bot = telebot.TeleBot("888729683:AAGYwRwy2xrDuZnD8PtD9-v0S2aDhBh9r-g")


def index_traffic(frame_number, output_array, output_count):
    """Функция поиска определенных объектов"""
    for i in output_count:
        print(i)
        if i == 'person' or 'car':
            send_photo(artur_id)
            send_photo(sofi_id)
            photo_cap()


def photo_cap():
    """Функция для фотографирования"""
    cap = cv2.VideoCapture(4)
    dt = datetime.now()
    for i in range(1):
        cap.read()
        ret, frame = cap.read()
        cv2.imwrite('/home/zico/PycharmProjects/untitled/photo/{}.jpeg'.format(str(dt.year) + "-" +
                                                                               str(dt.month) + "-" + str(dt.day) + "-" +
                                                                               str(dt.hour) + "-" + str(dt.minute) +
                                                                               "-" +
                                                                               str(dt.second) + "-" +
                                                                               str(dt.microsecond)), frame)
        print("Detected")
    cap.release()


def send_photo(id_1):
    """TELEGRAM send photo"""
    cap = cv2.VideoCapture(4)
    for i in range(1):
        cap.read()
        ret, frame = cap.read()
        cv2.imwrite("/home/zico/PycharmProjects/untitled/photo/001.jpeg", frame)
        link = "/home/zico/PycharmProjects/untitled/photo/001.jpeg"
        bot.send_photo(id_1, open(link, "rb"))
        # bot.send_photo(id_2, open(link, "rb"))
        cap.release()
    print("Sending")


def proxy():
    with open('/home/zico/PycharmProjects/untitled/proxy/proxy.txt', 'r') as inf:
        for line in inf:
            return line



camera = cv2.VideoCapture(2)
detector = VideoObjectDetection()
detector.setModelTypeAsRetinaNet()
detector.setModelPath( os.path.join(execution_path, "/home/zico/PycharmProjects/untitled/models/retina.h5"))
detector.loadModel(detection_speed='fast')

video_path = detector.detectObjectsFromVideo(camera_input=camera,
                                             output_file_path=os.path.join(execution_path, "traffic_detected"),
                                             frames_per_second=5, log_progress=True, display_object_name=True,
                                             per_frame_function=index_traffic,
                                             save_detected_video=False)

