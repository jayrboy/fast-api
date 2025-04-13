# Prediction

```bash
$ pip3 install fastapi openai sqlalchemy
```

# Test

```bash
curl -X POST http://localhost:8000/chat \
-H "Content-Type: application/json" \
-d '{"username": "jay", "message": "Tell me a joke"}'

```

# Tips

1. Image classifier
   - รับภาพผ่าน API แล้วให้โมเดล TensorFlow ทำนายคลาส
2. Text sentiment
   - วิเคราะห์ความรู้สึกจากข้อความ
3. Object detection
   - ส่งภาพมาให้ AI ตรวจจับวัตถุ
4. Chatbot
   - ทำระบบแชทที่เชื่อมกับโมเดลภาษา (เช่น T5, GPT แบบ Local)
5. Time-series forecast
   - ทำนายยอดขาย / อุณหภูมิ จากข้อมูลชุดหนึ่ง

# ถ้าไม่ใช้ TensorFlow

1. scikit-learn, เบา เร็ว ใช้ CPU ได้ดี, ML ทั่วไป เช่น classification, regression
2. onnxruntime, เร็ว รองรับหลาย format, รันโมเดล TF / PyTorch / sklearn
3. PyTorch, ยืดหยุ่น ใช้กับ DL ได้, DL เช่น image, text, time-series (Image Classifier)
4. Hugging Face, ใช้งาน NLP ได้ง่าย, sentiment, summarization, translation

# Reference

https://life.promptsnapshot.com/เจาะลึก-chatgpt-api-คู่มือตั้งแต่-basic-ถึง-advance-f23c5816f791
