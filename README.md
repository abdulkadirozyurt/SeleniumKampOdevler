#  Pytest Decorators
Test fonksiyonlarını ayarlamak, tanımlamak ve işaretlemek için kullanılan özel anotasyonlardır.

Bunları kullanarak test çıktılarını kontrol edebilir, test davranışlarını değiştirebilir veya test sürecini özelleştirebiliriz. 

## Pytest için bazı yaygın decorator gösterimleri

+ **@pytest.fixture:** Bu, testlerimize gerekli girdileri veya kaynakları sağlamak için kullanabileceğiniz özel bir fonksiyon veya işlevdir.
---
Daha iyi açıklamak gerekirse, test fonksiyonlartımızın başarıyla çalışabilmesi için belirli bir durum veya kaynak gerektirebiliriz. Örnek olarak bir test veritabanında çalışırken önceden hazırlanmış veritabanı bağlantısı gibi bir şeyi kullanmak istediğimizde bu decorator'ü kullanabiliriz.
 
---
**@pytest.fixture** decorator'ı; bir fonksiyonu, test fonksiyonlarınızın önceden şart koştuğu bir fonksiyon haline getirir. Bu fonksiyon, test fonksiyonlarınızın kullanabileceği verileri hazırlar ve test fonksiyonlarına sağlar. Örneğin, aşağıdaki kod, bir hesap makinesi uygulaması için bazı test fonksiyonlarına, hesap makinesinin işlevlerini gönderir.


``` 
import pytest

class Calculator:
    def __init__(self):
        self.result = 0

    def reset(self):
        self.result = 0

    def add(self, a, b):
        self.result = a + b
        return self.result

    def subtract(self, a, b):
        self.result = a - b
        return self.result

    def multiply(self, a, b):
        self.result = a * b
        return self.result

    def divide(self, a, b):
        self.result = a / b
        return self.result
    

@pytest.fixture
def calculator():
    # İlk adım olarak, bir hesap makinesi nesnesi oluşturuyoruz.
    calc = Calculator()
    # İkinci adım olarak, hesap makinesinin hazır olmasını sağlıyoruz.
    calc.reset()
    # Son olarak, hesap makinesi nesnesini test fonksiyonlarına döndürüyoruz.
    return calc

def test_addition(calculator):
    # Toplama işlemi testi
    assert calculator.add(2, 3) == 5

def test_subtraction(calculator):
    # Çıkarma işlemi testi
    assert calculator.subtract(3, 2) == 1

def test_multiplication(calculator):
    # Çarpma işlemi testi
    assert calculator.multiply(2, 3) == 6

def test_division(calculator):
    # Bölme işlemi testi
    assert calculator.divide(6, 3) == 2

```



+ **@pytest.mark.parametrize:** Aynı test fonksiyonunu farklı girdi verileri ile birden fazla kez çalıştırmak için kullanılır.

+ **@pytest.mark.skip:** Bir testi atlamak için kullanılır.

+ **@pytest.mark.xfail:** Bir testin bilinçli olarak başarısız olması gerektiğini belirtmek için kullanılır.

+ **@pytest.mark.timeout:** Bir testin belirli bir sürede tamamlanması gerektiğini belirtmek için kullanılır.

![TestinTab](https://raw.githubusercontent.com/abdulkadirozyurt/SeleniumKampOdevler/master/1.png)
