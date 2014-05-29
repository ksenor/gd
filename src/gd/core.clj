(ns gd.core)
(use 'clj-webdriver.taxi)

(defn fb-browser []
  (set-driver! {:browser :firefox} "https://fb.com"))

(defn fb-login [login_password_pair]
  (click "#email")
  (input-text "#email" (first login_password_pair))
  (click "#pass")
  (input-text "#pass" (second login_password_pair))
  (click "#u_0_n"))

(defn go-to-gd [] (to "https://www.facebook.com/www.GD.ru/photos/a.164373060283044.52122.151805011539849/665361856850826/"))