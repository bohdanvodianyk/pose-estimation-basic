import cv2
import mediapipe as mp
import time


class poseDetector():

    def __init__(self, mode=False, modelCompl=1, smooth=True, eneableSegmentation=False, smoothSegmentation=True,
                 detectionConf=0.5, trackingConf=0.5):

        self.mode = mode
        self.modelCompl = modelCompl
        self.smooth = smooth
        self.eneableSegmentation = eneableSegmentation
        self.smoothSegmentation = smoothSegmentation
        self.detectionConf = detectionConf
        self.trackingConf = trackingConf

        self.mpDraw = mp.solutions.drawing_utils
        self.mpPose = mp.solutions.pose
        self.pose = self.mpPose.Pose(self.mode, self.modelCompl, self.smooth, self.eneableSegmentation,
                                     self.smoothSegmentation, self.detectionConf, self.trackingConf)

    def findPose(self, img, draw=True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results = self.pose.process(imgRGB)
        print(results.pose_landmarks)
        if results.pose_landmarks:
            if draw:
                self.mpDraw.draw_landmarks(img, results.pose_landmarks,
                                           self.mpPose.POSE_CONNECTIONS)
                for id, lm in enumerate(results.pose_landmarks.landmark):
                    h, w, c = img.shape
                    cx, cy = int(lm.x * w), int(lm.y * h)
                    cv2.circle(img, (cx, cy), 10, (255, 0, 0), cv2.FILLED)
        return img




def main():
    cap = cv2.VideoCapture('PoseExamplesVideos/2.mp4')
    pTime = 0
    detector = poseDetector()

    while True:
        success, img = cap.read()
        img = detector.findPose(img)
        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime

        cv2.putText(img, str(int(fps)), (70, 50), cv2.FONT_HERSHEY_PLAIN, 3,
                    (255, 0, 0), 3)
        cv2.imshow("Image", img)

        cv2.waitKey(1)


if __name__ == "__main__":
    main()
