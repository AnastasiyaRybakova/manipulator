;; Auto-generated. Do not edit!


(when (boundp 'motor_control::Motor2)
  (if (not (find-package "MOTOR_CONTROL"))
    (make-package "MOTOR_CONTROL"))
  (shadow 'Motor2 (find-package "MOTOR_CONTROL")))
(unless (find-package "MOTOR_CONTROL::MOTOR2")
  (make-package "MOTOR_CONTROL::MOTOR2"))
(unless (find-package "MOTOR_CONTROL::MOTOR2REQUEST")
  (make-package "MOTOR_CONTROL::MOTOR2REQUEST"))
(unless (find-package "MOTOR_CONTROL::MOTOR2RESPONSE")
  (make-package "MOTOR_CONTROL::MOTOR2RESPONSE"))

(in-package "ROS")





(defclass motor_control::Motor2Request
  :super ros::object
  :slots (_order ))

(defmethod motor_control::Motor2Request
  (:init
   (&key
    ((:order __order) 0)
    )
   (send-super :init)
   (setq _order (round __order))
   self)
  (:order
   (&optional __order)
   (if __order (setq _order __order)) _order)
  (:serialization-length
   ()
   (+
    ;; int32 _order
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; int32 _order
       (write-long _order s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; int32 _order
     (setq _order (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;;
   self)
  )

(defclass motor_control::Motor2Response
  :super ros::object
  :slots (_id _position ))

(defmethod motor_control::Motor2Response
  (:init
   (&key
    ((:id __id) 0)
    ((:position __position) 0)
    )
   (send-super :init)
   (setq _id (round __id))
   (setq _position (round __position))
   self)
  (:id
   (&optional __id)
   (if __id (setq _id __id)) _id)
  (:position
   (&optional __position)
   (if __position (setq _position __position)) _position)
  (:serialization-length
   ()
   (+
    ;; int32 _id
    4
    ;; int32 _position
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; int32 _id
       (write-long _id s)
     ;; int32 _position
       (write-long _position s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; int32 _id
     (setq _id (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;; int32 _position
     (setq _position (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;;
   self)
  )

(defclass motor_control::Motor2
  :super ros::object
  :slots ())

(setf (get motor_control::Motor2 :md5sum-) "336caa623787c2e2b9bf54c39edf8455")
(setf (get motor_control::Motor2 :datatype-) "motor_control/Motor2")
(setf (get motor_control::Motor2 :request) motor_control::Motor2Request)
(setf (get motor_control::Motor2 :response) motor_control::Motor2Response)

(defmethod motor_control::Motor2Request
  (:response () (instance motor_control::Motor2Response :init)))

(setf (get motor_control::Motor2Request :md5sum-) "336caa623787c2e2b9bf54c39edf8455")
(setf (get motor_control::Motor2Request :datatype-) "motor_control/Motor2Request")
(setf (get motor_control::Motor2Request :definition-)
      "int32 order
---
int32 id
int32 position
")

(setf (get motor_control::Motor2Response :md5sum-) "336caa623787c2e2b9bf54c39edf8455")
(setf (get motor_control::Motor2Response :datatype-) "motor_control/Motor2Response")
(setf (get motor_control::Motor2Response :definition-)
      "int32 order
---
int32 id
int32 position
")



(provide :motor_control/Motor2 "336caa623787c2e2b9bf54c39edf8455")


