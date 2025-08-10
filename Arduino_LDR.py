import serial
import time 
try:
    ser=serial.Serial('COM3',9600,timeout=1)
    print(f"COM3 portu başarıyla açıldı.")
    time.sleep(2)
    for _ in range(5):
       ser.readline()
except serial.SerialException as error_:
    print(f"Seri porta bağlanılamadı.Lütfen COM3 portunu kontrol ediniz: {error_}")
    exit()
except PermissionError:
    print(f"Port erişimi engellendi.Lütfen kontrol ediniz.")
    exit()

LDR_esik_degeri=300
led_durumu=-1
def led_kontrol(ser,durum):
    global led_durumu
    if durum!=led_durumu:
        try:
            if durum==1:
                ser.write(b'1')
                print(f"Led yanıyor.")
            else:
                ser.write(b'0')
                print(f"Led söndürüldü.")
            led_durumu=durum
        except Exception as error_:
            print(f"Led kontrol hatası: {error_}") 

def ldr_degeri_oku(ser):
    try:
     veri_satiri=ser.readline()
     metin_veri=veri_satiri.decode('utf-8').strip()
     if metin_veri and metin_veri.isdigit():
        return int(metin_veri)
     return None
    except UnicodeDecodeError:
     print(f"Hata: Seri portta okunan veri bozuk ya da hatalı.")
    except Exception as e:
     print(f" Okuma sırasında beklenmeyen bir hata oluştu:{e}")
    return None   
try:
    print(f"\n LDR değerleri okunmaya başlandı.")
    while True:      
     ldr_degeri=ldr_degeri_oku(ser)
     if ldr_degeri is not None:
      if ldr_degeri<LDR_esik_degeri:
       led_kontrol(ser,1)
       print(f"Led yanar ve Arduinodan gelen LDR değeri: {ldr_degeri}'dir.")        
      else:
       led_kontrol(ser,0)
       print(f"Led söner ve Arduinodan gelen LDR değeri:{ldr_degeri}'dir.")

     time.sleep(0.05)
except KeyboardInterrupt:
   print(f"\n Program sonlandırıldı.")
except Exception as ex:
   print(f"Hata: Beklenmeyen bir hata oluştu: {ex}")
finally:
   if 'ser' in locals() and ser.is_open:
     try:
      ser.write(b'0')
      time.sleep(0.1)
     except Exception as e:
      print(f"Hata LED kapanırken bir sorun oluştu: {e}")
     ser.close()
     print(f"Seri port kapatıldı.")        


