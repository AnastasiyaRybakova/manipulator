
(cl:in-package :asdf)

(defsystem "motor_control-srv"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "Motor2" :depends-on ("_package_Motor2"))
    (:file "_package_Motor2" :depends-on ("_package"))
  ))