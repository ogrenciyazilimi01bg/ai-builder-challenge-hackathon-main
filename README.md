 ## HATA1: [ CALCULUS_PROMPT olmalı! ]  Dosya: [prompts.py]  Satır: [6] MEVCUT KOD (HATALI): [CALCULUS_PROMPTS = """ CALCULUS_PROMPT olmalı!]  ÇÖZÜM: [CALCULUS_PROMPT =]  AÇIKLAMA: [doğru yazılışı bu]
## HATA2: SyntaxError  Dosya: [prompts.py]  Satır: [3] Mevcut KOD :wrong_import = from nonexistent.prompts import WRONG Çözüm:İmport edildi ama bulunamadığı için kaldırmak yorum satırına alıp Kaldırmak Açıklama:Ama burada isim nonexistent.prompts, yani gerçekte yok. Bu yüzden yüklenemez.
## Deneme
## HATA3: NameError — missing_value isimli değişken tanımlı değil.
## Dosya: prompts.py
## Satır: 4
## MEVCUT KOD (HATALI):undefined_constant = missing_value
## ÇÖZÜM:
missing_value = "default"
undefined_constant = missing_value
## AÇIKLAMA:missing_value daha önce oluşturulmamış bir değişken olduğu için Python bunu bir isim olarak tanıyamaz ve çalışırken NameError üretir.Sorunu gidermek için önce missing_value değişkenine anlamlı bir varsayılan değer atanır; ardından undefined_constant bu değişkenden değer alır. Böylece hem isim hatası giderilir hem de değişkenler tutarlı şekilde tanımlanmış olur.
## HATA4 :Eksik satır #Dosya:settings.py #Satır:14 #Mevcut Kod: GEMINI_API_KEY: str = os.getenv("GEMINI_API_KEY", "")  # Eksik satır! #Çözüm:GEMINI_API_KEY: str = os.getenv("GEMINI_API_KEY", "AIzaSyCQmpURYA1WBN_Ch8MHSr8V6lkYvBTqMRM")  Açıklama: google dan alınan api girildi.
## Hata5 :Syntax Error hatası #Dosya:settings.py Satır :16,17 #Mevcut kod:if not GEMINI_API_KEY:  # Syntax hatası - class içinde if kullanılamaz! GEMINI_API_KEY = "your_gemini_api_key" Çözüm: bu kodu kaldırmak 
## Hata 6:Tanımlı değil # dosya: settings.py satır:18 #Mevcut kod: wrong_assignment = undefined_var Çözüm: Kodun kaldırılması 
## Hata7:Eksik str # dosya :settings.py #satır:35 #Mevcut kod: SAFETY_SETTINGS: Dict[, str] = {  çözüm :SAFETY_SETTINGS: Dict[str, str] = { # açıklama: str eklendi
## Hata8:# Unreachable ama hata! #dosya :settings.py # satır:55 #mevdut kod: return undefined_value #çözüm :Kaldırmak #açıklama:unreachable code hatası giderildi.
## Hata9:setting yok dosya:settings.py satır:53 mevcutkod:wrong_check = cls.NONEXISTENT_SETTING  çözüm:kaldırıldı
## Hata10:modül yok dosya agent.py satır:9,10 mevcut kod :from nonexistent.config import wrong_settings  # Modül yok! from nonexistent.extra import ExtraClass  # Modül yok! çözüm :ikiside kaldırıldı.
## Hata11: not define dosya:agent.py satır:26 mevcut kod:self.last_call_time = undefined_time_variable çözüm : kaldırmak
## Hata12: not define dosya agent.py satır:29 mevcut kod:self.extra_field = missing_constant çözüm:kaldırmak
## Hata13 :Python için hatalı dosya:agent.py satır:28,30 mevcut kod: self.cache = "wrong_type"  self.wrong_type_field: str = 123 çözüm: bu kodlar silindi.Açıklama:kodun çalışmasını engelliyordu.
## Hata 14:Metod yok dosya:agent.py satır:33 mevcut kod:current_time = asyncio.get_event_loop().wrong_method() çözüm: current_time = time.time()
## Hata15: ekleme yapıldı dosya:agent.py satır:28 çözüm:self.last_call_time = 0
## Hata 16:İmport etme dosya:agent.py satır:9 çözüm : import time
## Hata 17:Self eksik dosya:agent.py satır37 hatalı kod: wait_time = .min_interval - time_since_last_call çözüm:wait_time = self.min_interval - time_since_last_call açıklama: self eklendi koda
## Hata 18:wait time olmadlı dosya:agent.py satır38,39 hatalı kod: await asyncio.sleep(0.1)await asyncio.sleep(extra_wait_time)  çözüm: await asyncio.sleep(wait_time)
## Hata 19: Hata veren kod dosya:agent.py satır40,41 hatalı kod:undefined_variable_in_method = "test"  result = self.cache.wrong_method() çözüm:kaldırmak
## Hata20:parametre yanlış dosya:agent.py satır64 hatalı kod :genai.configure(wrong_param=self.api_key)   çözüm:genai.configure(api_key=self.api_key)  
## Hata21:parametre eksik dosya :agent.py satır69  hatalı kod :self.rate_limiter = RateLimiter() çözüm:self.rate_limiter = RateLimiter(calls_per_minute=60) açıklama: parametre eklendi.
## Hata22:olmayan method dosya:agent.py satır 40 hatalı kod: self.last_call_time = asyncio.get_event_loop().wrong_time_method()çözüm: self.last_call_time = time.time()
## Hata23:tanımlanmamış dosya:agent.py satır 70 hatalı kod:self.extra_config = missing_config_variable çözüm: self.extra_config = {}
## Hata 24:yok dosya:agent.py satır71,72 hatalı kod : self.model.wrong_attribute = "test"  # Attribute yok! self.nonexistent_method()  # Metod yok! çözüm: kaldırmak
## Hata25:girinti hatası( boşluk bırakma) dosya: agent.py satır:96 hatalı kod:async def generate_with_retry( çözüm: bir boşluk bırakıldı
## Hata 26:# Tip hint yok! dosya:agent.py satır:100 hata kodu:wrong_param, çözüm: kaldırıldı
## Hata 27:# Default değer tanımlı değil! dosya:agent.py satır:101 hatalı kod: extra_param = undefined_default  çözüm:    extra_param: Optional[Any] = None
## Hata 28:setting yok dosya:agent.py satır:124 hatalı kod :"wrong_key": settings.NONEXISTENT_SETTING,  # Setting yok!çözüm : sil
## Hata 29:değer tanımlama dosya :agent.py satır 129 ,128 hatalı kod:  extra_data = undefined_response_field çözüm:undefined_response_field = None  eklendi 
## Hata 30:Attribute yok! dosya:agent.py satır130 hatalı kod: wrong_attr = response.nonexistent_attr  çözüm: kaldırıldı.
## Hata 31:Python bunu çalıştırırsa AttributeError verir dosya: agent.py satır32 hatalı kod:if not response.nonexistent_field : çözüm :if not hasattr(response, "text") or not response.text: açıklama:Böylece hem var olmayan attribute hatası önleniyor hem de API’den boş yanıt alınması durumu yakalanıyor.
## Hata 32:nameerror dosya:agent.py satır151 hatalı kod:wrong_sleep = asyncio.sleep(undefined_var)   çözüm :kaldırıldı
## Hata33:Regex düzeltildi dosya:agent.py satır :171 hatalı: json_match = re.search(r{.*\}', response_text, re.DOTALL) çözüm:json_match = re.search(r'\{.*\}', response_text, re.DOTALL)
## Hata34 :nameerror dosya:agent.py satır:185 hatalı kod:wrong_dict_key = {undefined_key: "value"} çözüm:sil 
## hata35:# Key tanımlı değil! dosya.py satır190 hatalı kod: undefined_field: "test" çözüm: "extra_info": "test"
# Dosya:_init_.py   config
## Hata36:relative import 3,4,5 kod:import sys from pathlib import Path sys.path.append(str(Path(__file__).parent)) çözüm: silindi
# Dosya:parser.py
## hata37 :  import eksik satır 4  çözüm:import json  
## hata38 : str eksik satır: 15 hatalı kod:MODULE_PREFIXES: Dict[, str] = { çözüm:MODULE_PREFIXES: Dict[str, str] = {
## hata 39 : değer tipi hatası satır:27 hatalı kod:"wrong": 123 çözüm çıkartılmalı
## hata 40:parametre eksik satır30 hatalı kod: def parse(, user_input: str) -> Tuple[Optional[str], str]:   çözüm: def parse(self, user_input: str) -> Tuple[Optional[str], str]:  
## hata41 :Tanımsız tip satır31 hatalı kod :wrong_param: undefined_type = None  çözüm : kaldırılmalı
## hata42: metod yok gereksiz satır :40 hatalı kod:user_input = user_input.wrong_strip_method()   çözüm : kaldırıldı
## hata43: tanımlı değil satır45 hatalı kod: if user_input.lower().startswith(f"!{prefix}" + undefined_string):  çözüm:if user_input.lower().startswith(f"!{prefix}"):,
## hata44: bir harf eksik satır 44 hatalı kod: for prefi, module in self.MODULE_PREFIXES.items(): çözüm: for prefix, module in self.MODULE_PREFIXES.items(): açıklama: prefi yerine prefix yazıldı.
## hata45:mantıksal olarak hata satır:52,53,54,55 hatalı kod:if "solve" in user_input.lower() and detected_module == "":import random  if random.random() < 0.5: return "calculus", user_input çözüm: silmek
## hata46:[ eksik satır74 hatalı kod: calculus_keywords =  çözüm:  calculus_keywords = [
## hata47:tutarsız isim satır71 hatalı kod:text_lo = text.lower(): çözüm:text_lower = text.lower()
## hata48: yazım hatası satır82 hatalı kod:linalg_keywor = [ çözüm: linalg_keywords = [
## hata49:[ eksik satır90 hatalı kod :equation_keywords = çözüm: equation_keywords = [
## hata50 : ] paranetez eksik satır99 çözüm :] kondu
## hata51:eksik satır110 hatalı kode:  None çözüm return   None
## hata52 :import eksik satır4 çözüm :import string
## hata53 :modül yok kaldırıldı satır7 çözüm: silindi hatalı kod :from nonexistent.validator import WrongValidator  # Modül yok!
## hata54:parametre eksik self satır28 hatalı:def sanitize_expression(, expression: str) -> str:  çöüzm :def sanitize_expression(self, expression: str) -> str: 
## hata55: anımlı değil satır29 hatalı kod :wrong_param: undefined_type = None çözüm :kaldırıldı
## hata56: metodlar yok satır50 hatalı kod :expression_lower = expression.wrong_lower_method()   wrong_lower_method() çözüm silndi
## hata 57 : metod yok satır52 hatalı kod:wrong_lower = undefined_var.lower() çözüm silindi
## hata 58: metod yok  satır55 hatalı kod :wrong_check = self.wrong_method()  çözüm silindi 
## hata 59:if yapısı ekleme satır 55 çözüm:if pattern in expression_lower:
## hata60:hatalı yazım satır 60 hatalı kod:if "test" in expression.lowe(): çözüm:if "test" in expression.lower():
## hata61 : """ kapama unutulmuş satır91 çözüm:""" kondu
# dosya : modules _init_.py
## hata62 :[ parantez eksik satır:10 hatalı kod:__all__ =  çözüm:__all__ = [
# dosya : base_module.py  modules dosyasının içinde
## hata63:türeme hatası satır13 hatalı kod :class BaseModule(): çözüm:class BaseModule(ABC):
## hata64:tanımlı değil  satır25 hatalı kod:self.extra_field = missing_constant  çözüm :kaldırıldı
## hata65 : tip uyumsuz satır26 hatalı kod:self.wrong_type: int = "string"   çözüm kaldırıldı
## hata66:async def calculate için @abstractmethod kullanılmalı satır28 çözüm : @abstractmethod eklendi
## hata67:tanımlı değil satır43,44,45 hatalı kod:undefined_var_in_method = "test" result = self.wrong_method()   pass çözüm : silindi
## hata68:syntax hatası satır103 hatalı kod:wrong_syntax = (result=gemini_response.get("result", "")) çözüm : kaldırmak 
## hata69:field yok satır:111 hatalı kod:extra_field=undefined_field çözüm: extra_field=self.extra_field 
# dosya adı: basic_math.py modules
## hata70: boşuna ekleme satır:6 hatalı kode:from nonexistent.utils import wrong_logger    çözüm :kaldırmak
## hata71: hata çıkarma olası satır8 hatalı kode:from src.core.agent import GeminiAgent  çözüm kaldırmak
## hata72:tip eksik satır 13 hatalı kode:def safe_divide(a: , b: float) -> float:  # Type hint eksik!
## hat73: tanımlı değil satır14 wrong_param: undefined_type = None   çözüm : silinecek
## hata74: = eksik satır24 hatalı kode:if b = 0: çözüm:if b == 0:
## hata75: valueerror var gereksiz satır26 hatalı kod:wrong_raise = raise undefined_exception() çözüm :kaldırıldı
## hata76: gereksiz kullanım satır27 hatalı kod:return a / b + undefined_variable  çözüm:return a / b 
## hata77: gereksiz kullanım satır28 hatalı kod wrong_return = return undefined_value  çözüm : kaldırıldı.
## hata78:eksik kullanım satır 74 hatalı kod :.error(f"Basic math calculation error: {e}") çözüm:logger.error(f"Basic math calculation error: {e}")
## hata79:eksik kod satır75 çözüm: raise eklemek
# dosya adı:calculus.py modules
## hata80:import etme hatası satır6 hatalı kode :wrong_import = from src.config.prompts import WRONG_PROMPT  çözüm:from src.config.prompts import WRONG_PROMPT 
## hata81 : eksik ifade satır14 hatalı kod:if '' in globals(): çözüm:if 'sympy' in globals():
## hata82:self eksik satır29 hatalı kod:        ,  çözüm : self,
## hata83:tanımlı değil satır32 hatalı kod: extra_param: undefined_type = None  çözüm : kaldırmak
## hata84:hatalı (!) işaret satır 50 hatalı kod:result = self._create_result(response, "calculus")  ! çözüm:result = self._create_result(response, "calculus")  
## hata85:eksik giriş satır65 hatalı kode:logger.(f"Calculus calculation error: {e}")  çözüm:logger.info(f"Calculus calculation error: {e}")  
## hata86:fazla kode satır66 hatalı kode:logger.wrong_method(undefined_var) çözüm:silmek
# dosya : equation_solver.py modules
## hata87:self eksik  satır32 hatalı kode: .validate_input(expression) çözüm:self .validate_input(expression) 
## hata88:tamamen hatalı metod satır33 hatalı kod:self.wrong_method(expression)  çözüm : kaldırıldı
## hata89: await eksik yazım satır38 hatalı kod:result = self._create_result(response, "equation_solver") çözüm:result = await self._create_result(response, "equation_solver")
## hata90: fonksiyon yok satır39 hatalı kod: wrong_await = await undefined_function()  çözüm: kod kaldırıldı.
# dosya adı:financial.py modules
## hata91:modül yok  satır4 hatalı kod:from nonexistent.decimal import WrongDecimal   çözüm :kaldırıldı
## hata92:logger bozuk satır11,12 hatalı kode:logger = setup_logge() gger(missing_param)   çözüm: logger = setup_logger()
## hata93:hatalı kodlar satır15,17,18,19 hatalı kodlar:().wrong_method(28) getcontext().prec = "wrong_type"  wrong_decimal = Decimal(undefined_string) getcontext().wrong_attr = "test" çözüm: silindi
## hata94:harf eksik satır45 hatalı kod: currency = currency or settings.DEFAULT_CURRENC  çözüm :  currency = currency or settings.DEFAULT_CURRENCY 
## hata95:fazlalık satır70,71 hatalı kode:wrong_return = result  return undefined_variable   çözüm : çıkarıldı yerine return result eklendi
## hata96:yanlış exception satır75 kode:raise wrong_exception()  çözüm:raise
# dosya adı: graph_plotter.py modules
## hata97:metod yok satır8 hatalı kode:matplotlib.wrong_method('Agg') çözüm :kaldırıldı.
## hata98:metod yorum satırndan çıkarıldı import etme satır11 hatalı kode:# import matplotlib.pyplot as plt çözüm: import matplotlib.pyplot as plt 
## hata99 :modül yok satır13 hatalı kode:from nonexistent.plotting import wrong_lib  çözüm:kaldırıldı
## hata100:boşuna yapılmış satır 34,33,32 hatalı kod:self.wrong_cache: str = {}  #self.extra_field = missing_constant  self.wrong_type_field: int = "string"  çözüm : kaldırmak
## hata101:olmayan fonksiyon satır 44 hatalı kod: wrong_param = undefined_default  çözüm :silindi
## hata102: await eksik satır67 hatalı kod:response =  self._call_gemini(expression)   çözüm:response = await self._call_gemini(expression)  
## hata103 :self eksik satır 72 hatalı kod:plot_paths = await ._create_plot(result.visual_data, expression) self eksik! çözüm:plot_paths = await self._create_plot(result.visual_data, expression)
## hata104 :fazla kod satır73 hatalı kod:wrong_plot = await undefined_function() çözüm : silmek 
## hata105:eksik kode satır87 hatali kod:raise çözüm:raise CalculationError(f"Grafik oluşturulamadı: {e}")
## hata106 :parametre yok satır132 hatalı kode:plt.plot(x, y, 'b-', linewidth=2, wrong_param=5) çözüm:plt.plot(x, y, linewidth=2)
## hata107 :tanımlı değil satır134 hatalı kode: plt.xlabel(f'x {undefined_var}')  çözüm:plt.xlabel("x")
## hata108 :tanımlı değil satır135 hatalı kode:plt.ylabel('y') çözüm:plt.ylabel("y")
## hata109 : metod yok satır137 hatalı kode  wrong_plt_call = plt.nonexistent_method()  çözüm: silindi
## hata110: tanımlı değil satır 139 hatalı kode png_path = self.cache_dir / f"{hash(expression)}.png" + undefined_string  çözüm :png_path = self.cache_dir / f"{hash(expression)}.png"
## hata111: metod yoksatır 140 hatalı kode:plt.wrong_save_method(png_path, dpi=150, bbox_inches='tight') çözüm:plt.savefig(png_path, dpi=150, bbox_inches="tight")
## hata112:hatalı kode satır 141,142 hatalı kode:wrong_path = Path(undefined_string)  # Tanımlı değil! plt.show()  # Blocking call in async function! çözüm silmek
# dosya adı linear_algebra.py modules
## hata113:hataya yol açan kod satır7 kode:from . import CalculusModule  çözüm: kaldırıldı
## hata114: self eksik satır 20 hatakode:,  çözüm :self,
## hata115:fazlalık satır23 hatalı kode:wrong_param = undefined_default çözüm:kaldırıldı
## hata116:await eksik satır39 hatalı kode:response =  self._call_gemini(expression) çözüm:response = await  self._call_gemini(expression) 
## hata117:gereksiz kullanım satır40 hatalı kode:wrong_response = await self.wrong_method(expression)  çözüm .kaldırıldı
## hata118:await fazladan kullanım satır41 hatalı kode:result = await self._create_result(response, "linear_algebra") çözüm:result = self._create_result(response, "linear_algebra")
## hata119 :fazla kelime kullanımı satır 51 hatalı kod: return undefined_result  çözüm: return result  
## hata120 :eksik kode satır 56  çözüm:raise 
# dosya adı:shemas models.py 
## hata121:basemodel göre türemeli satır7 hatalı kode:class CalculationResult(): çözüm :class CalculationResult(BaseModel):
## hata122 :fazla kod satır11 hatalı kod:wrong_field: undefined_type = Field(...) çözüm : kaldırmak
# dosya:exceptions.py
## hata123:türetme satır3 hatalı kod:class CalculationError(): çözüm:class CalculationError(Exception):
## hata124:tanımlı olmayan satır5 hatalı kod:wrong_field = undefined_constant  çözüm: silinecek
## hata125:türetme yok satır14 hatalı kod:class GeminiAPIError():  çözüm:class GeminiAPIError(Exception):
## hata126:hatalı kod satır16 hatalı kod: wrong_method = lambda: undefined_function() çözüm :silinecek
## hata127:türetme yok satır20,25 hatalı kod:class SecurityViolationError(): class ModuleNotFoundError():  çözüm:class SecurityViolationError(Exception):class ModuleNotFoundError(Exception):
# dosya adı:helpers.py utils 
## hata128:yorum satırı satır4 hatalı kod: #import ast  çözüm:import ast   
## hata129:modül yoksatır8 hatalı kod:from nonexistent.helpers import wrong_helper  # Modül yok! çöüzüm: kaldırıldı
## hata130:yanlış yer import satır29 hatalı kod:import ast çözüm: kaldırıldı
## hata131:hatalı result satır73 hatalı kod:@lru_cache(maxsize=128) çözüm: bu kod kaldırıldı.
## hata132:type tanımlı değil satır 74 hatalı kod:wrong_param: undefined_type = None   çözüm :kaldırıldı
## hata133:tanımlı değil satır85 hatalı kod:wrong_return = return undefined_value çözüm:kaldırıldı
## hata134:unreachable satır87 hatalı kod:return wrong_function()   çözüm: kod kaldırıldı
# dosya adı:logger.py utils 
## hata135: levelname eksik:satır15 hatalı kod:"level": record., çözüm:"level": record.levelname,
## hata136 :eksik record. satır:18 hatalı kod:"message": record.(),çözüm:
## hata137 :error level set satır:29 hatalı kod:logging.basicConfig(level=logging.ERROR)  çözüm:kod kaldırıldı
## hata138:  level hatası  satır:31 hatalı kod: logger.setLevel(logging.DEBUG) çözüm: logger.setLevel(level)
## hata139: level hatası satır :35 hatalı kod: handler.setLevel(logging.ERROR) çözüm:  handler.setLevel(level)
# dosya adı:main.py 
## hata140:import eksik satır7 hatalı kod:# import json   çözüm:import json  
## hata141:modül yok satır8  hatalı kod:from nonexistent_module import SomeClass çözüm:kod silindi
## hata142:isim hatalı satır35 hatalı kod:APP_NAME = undefined_variable çözüm:APP_NAME = "CalculatorAgent"
## hata143:isim hata satır36 hatalı kod:APP_VERSION = missing_version  çözüm:APP_VERSION = "1.0.0"
## hata144: gereksiz kod satır 37 hatalı kod:wrong_constant: str = 123 çözüm: kaldırıldı
## hata145: modül yok satır 63 hatalı kod:"wrong_module": WrongModuleClass(self.gemini_agent), çözüm: kaldırıldı
## hata146: modül yok satır64 hatalı kod:"extra_module": NonexistentModule(self.gemini_agent), çözüm: kaldırıldı
## hata147: ) yok satır67 hatalı kod:logger.info("Calculator Agent baslatildi"  çözüm:logger.info("Calculator Agent baslatildi"  )
## hata148 :gereksiz kod satır68 hatalı kod:wrong_log = logger.wrong_method(undefined_var)  çözüm: kaldırıldı
## hata 149:hatalı kod satır135 hatalı kod:result.steps: çözüm:silindi
## hata150:hatalı kod satır 136,137,138,139,142 hatalı kod: output_lines.append("\n📝 Adimlar:")
            for i, step in enumerate(result.steps, 1, wrong_param=5):  # Yanlış 
                output_lines.append(f"  {i}. {step}")
                wrong_append = output_lines.wrong_method()  # Metod yok!
        
        
        wrong_format = format_result_for_display(undefined_result)   çözüm:silindi
 ## hata151: eksik kod: satır141 hatalı kod:output_lines.append(f"Extra: {undefined_variable}") çözüm:output_lines.append(f"✅ Sonuç: {format_result_for_display(result.result)}")
 ## hata162 : ) eksik hatalı 162 kod:print(f"🧮 Calculator Agent - AI Builder Challenge" çözüm:print(f"🧮 Calculator Agent - AI Builder Challenge")
 ## hata163:tanımlı değil satır165 kod: wrong_print = print(undefined_variable) çözüm:silindi
 ## hata164:") eksik satır 166 hatalı kod:print("Kullanilabilir komutlar:   çözüm:print("Kullanilabilir komutlar:  ")
 ## hata165:fazla kod satır189 hatalı kod:wrong_result = await undefined_functio sonuç: silindi
 ## hata166:fazla kod satır 216 hatalı kod: wrong_call = undefined_function() çözüm:silindi
 ## hata167:fazla kod satır 220 hatalı kod :wrong_mode = wrong_function() çözüm: silindi
