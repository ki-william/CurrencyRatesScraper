from fixerio import Fixerio
import sys
import config as config


cur = config.db.cursor()
#Scraping the Rates from the API
symbols =  ['AED', 'AFN' , 'ALL' ,'AMD' ,'ANG' ,'AOA' ,'ARS' ,'AUD' ,'AWG' ,'AZN' ,'BAM' ,'BBD' ,'BDT' ,'BGN' ,	'BHD' ,	'BIF' ,	'BMD' ,	'BND' ,	'BOB' ,'BRL' ,	'BSD' ,	'BTN' ,	'BWP' ,	'BYR' ,	'BZD' ,	'CAD' ,	'CDF' ,	'CHF' ,	'CLF' ,	'CLP' ,	'CNY' ,	'COP',	'CRC' ,	'CUP' ,	'CVE' ,	'CZK' ,	'DJF' ,	'DKK' ,	'DOP' ,	'DZD' ,	'EGP' ,	'ETB' ,	'EUR' ,	'FJD' ,	'FKP' ,	'GBP' ,	'GEL' ,	'GHS' ,	'GIP' ,	'GMD' ,	'GNF' ,	'GTQ' ,	'GYD' ,	'HKD' ,	'HNL' ,	'HRK' ,	'HTG' ,	'HUF' ,	'IDR' ,	'ILS' ,	'INR' ,	'IQD' ,	'IRR' ,	'ISK' ,	'JEP' ,	'JMD' ,	'JOD' ,	'JPY' ,	'KES' ,	'KGS' ,	'KHR' ,	'KMF' ,	'KPW' ,	'KRW' ,	'KWD' ,	'KYD' ,	'KZT' ,	'LAK' ,	'LBP' ,	'LKR' ,	'LRD' ,	'LSL' ,	'LTL' ,	'LVL' ,	'LYD' ,	'MAD' ,	'MDL' ,	'MGA' ,	'MKD' ,	'MMK' ,	'MNT' ,	'MOP' ,	'MRO' ,	'MUR' ,	'MVR' ,	'MWK' ,	'MXN' ,	'MYR' ,	'MZN' ,	'NAD' ,	'NGN' ,	'NIO' ,	'NOK' ,	'NPR' ,	'NZD' ,	'OMR' ,	'PAB' ,	'PEN' ,	'PGK' ,	'PHP' ,	'PKR' ,	'PLN' ,	'PYG' ,	'QAR' ,	'RON' ,	'RSD' ,	'RUB' ,	'RWF' ,	'SAR' ,	'SBD' ,	'SCR' ,	'SDG' ,'SEK' ,'SGD' ,'SHP' ,'SLL' ,'SOS' ,'SRD' ,'STD' ,'SVC' ,'SYP' ,'SZL' ,'THB' ,'TJS' ,'TMT' ,'TND' ,'TOP' ,	'TRY' ,'TTD' ,'TWD' ,'TZS' ,'UAH',	'UGX','USD' ,'UYU' ,'UZS' ,'VEF' ,	'VND' ,	'VUV' ,	'WST' ,'XAF' ,	'XCD' ,'XDR' ,	'XOF','XPF' ,'YER' ,'ZAR' ,'ZMK' ,'ZWL' ]
convertFrom = str(sys.argv[1])
ConvertTo = 'EGP'
if convertFrom in symbols :
    fxrio = Fixerio(access_key='4901a054956048d6cdbd8a55db64709b')
    Rates = fxrio.latest(symbols=[ConvertTo ,convertFrom])  #the function always returns decitonry #the base always EUR
    isConvertedTo_Rate =  Rates['rates'][ConvertTo]
    ConvertedFrom_Rate =  Rates['rates'][convertFrom]
    CovertedFrom_Rate_referedToBase = 1/ConvertedFrom_Rate
    finalRate = CovertedFrom_Rate_referedToBase  * isConvertedTo_Rate
    print ("1 "+convertFrom+" = "+str(finalRate)+" "+ConvertTo)
    #Update the DB
    sql = "INSERT INTO RATES(rate) VALUES (%f) WHERE currency='%s'" %(finalRate,convertFrom)
    cur.execute(sql)
else : 
    print("Wrong currency symbol!!")


#setup the DB in docker image 
#write a test cases 