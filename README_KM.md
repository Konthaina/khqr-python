# konthaina-khqr (ខ្មែរ)

បណ្ណាល័យ Python សម្រាប់បង្កើត **KHQR payload string** (EMVCo TLV) សម្រាប់ Bakong / Cambodia និងមាន **CRC16 (CRC-16/CCITT-FALSE)** សម្រាប់ Verify។

> កញ្ចប់នេះបង្កើត “payload string” តែប៉ុណ្ណោះ។ អ្នកអាចយក payload ទៅ encode ជា QR image ដោយប្រើ library `qrcode`។

## ដំឡើង

```bash
pip install konthaina-khqr
```

បើចង់ generate QR image (PNG):

```bash
pip install "konthaina-khqr[qrcode]"
```

## ឧទាហរណ៍

```python
from konthaina_khqr import KHQRGenerator, MerchantType, Currency

result = (
    KHQRGenerator(MerchantType.INDIVIDUAL)
    .set_bakong_account_id("john_smith@devb")
    .set_merchant_name("John Smith")
    .set_currency(Currency.USD)
    .set_amount(100.50)
    .generate()
)

print(result.qr)
```

## Verify

```python
from konthaina_khqr import verify
print(verify(result.qr))
```
