import openai
import requests

class openaisor:
    def soru(self,kategori1,kategori2,kategori3,puan1,puan2,puan3): 
        # API anahtarınızı burada belirtin
        openai.api_key = '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'

        # Sormak istediğiniz soruyu burada tanımlayın
       
        if kategori1 == "" or kategori2=="" or kategori3=="":
            if kategori1=="":
                if kategori2=="":
                    if kategori3=="":
                        question = ""
                    else:
                        question = f"bana '{kategori3}' kategorisinde 10 da {puan3} lık olan sadece bir film öner filmin ismi ingilizce olsun sadece filmin ismini yaz."
                        
            
                elif kategori3=="":
                    question = f"bana '{kategori2}' kategorisinde 10 da {puan2} lık olan sadece bir film öner filmin ismi ingilizce olsun sadece filmin ismini yaz."
                else:
                    question = f"bana '{kategori2}' kategorisinde 10 da {puan2} lık ve {kategori3} kategorisinde 10 da {puan3} lık olan sadece bir film öner filmin ismi ingilizce olsun sadece filmin ismini yaz."
                    
            elif kategori2=="":
                if kategori3=="":
                    question = f"bana '{kategori1}' kategorisinde 10 da {puan1} lık olan sadece bir film öner filmin ismi ingilizce olsun sadece filmin ismini yaz."
                else:
                    question = f"bana '{kategori1}' kategorisinde 10 da {puan1} lık ve {kategori3} kategorisinde 10 da {puan3} lık olan sadece bir film öner filmin ismi ingilizce olsun sadece filmin ismini yaz."
            elif kategori3 =="":
                question = f"bana '{kategori1}' kategorisinde 10 da {puan1} lık ve {kategori2} kategorisinde 10 da {puan2} lık olan sadece bir film öner filmin ismi ingilizce olsun sadece filmin ismini yaz."
            else:
                question = f"Bana '{kategori1}' kategorisinde 10 da {puan1} lık ve '{kategori2}' kategorisinde 10 da {puan2} lık ve '{kategori3}' de 10 da {puan3} lık olan sadece bir film öner filmin ismi ingilizce olsun sadece filmin ismini yaz."
        else:
            question = f"Bana '{kategori1}' kategorisinde 10 da {puan1} lık ve '{kategori2}' kategorisinde 10 da {puan2} lık ve '{kategori3}' de 10 da {puan3} lık olan sadece bir film öner filmin ismi ingilizce olsun sadece filmin ismini yaz."
                      
        if question=="":
            answer = ""
            
        else:
             # OpenAI API'sine istek gönderin
            response = openai.Completion.create(
                engine="text-davinci-003",  # GPT-3 davinci modelini kullanabilirsiniz
                prompt=question,
                max_tokens=100,  # İstenen cevap uzunluğunu burada belirleyebilirsiniz
            )

            # OpenAI'nin cevabını alın
            answer = response.choices[0].text
    
        return answer       
        
            
                                
            
            
            
            
            
            
           
            
            
           



        
                
    