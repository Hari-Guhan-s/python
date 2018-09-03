import base64
import httplib2
import urllib2
import logging
import json
from openerp.osv import osv
from openerp.tools.translate import _
import equest_validations
import helper
import logging
import traceback
import werkzeug.utils
return_codes={
      '201' : 'Accepted',
      '401' : 'Authentication Failed',
      '202' : 'Accepted',
      '204' : 'Deleted' ,
      '200':'Ok'    
      }

def parameter_details(cr,uid):
     cr.execute(""" select url,user_name,password from hr_adm_job_posting_parameters where  status = 'Active' """)
     details = cr.dictfetchall()
     if details:
         return details
     else :
         return False
def post_job(self,cr,uid,data):
    result=" "
    if data:
        validate_obj = equest_validations.EquestValidations()
        if data:
            validate_result= validate_obj.validate(data)
        else :
            validate_result = "Please provide job or board data"
        if isinstance(validate_result, (bool)): 
            data_map_obj = helper.EquestDataMap()
            job_map = data_map_obj.get_equest_job_map_data(data)
            
        else:
            return validate_result
        logging.info(validate_result)
#             url=self.pool.get('ir.config_parameter').get_param(cr,uid,'eQuest _url')   
#             if url:
        
        #post_url_obj_ext =  'https://joblauncher.testing.equest.com/api'
        post_body = job_map
#             post_board_body=board_map['boards']
#             username=self.pool.get('ir.config_parameter').get_param(cr,uid,'eQuest_user_name')
#             password=self.pool.get('ir.config_parameter').get_param(cr,uid,'eQuest_password')    
        
        try:
            draft_res=create_draft_job(self,cr,uid,post_body)
#                 if (draft_res):
            if isinstance(draft_res, dict):
                
#                     return { 'type': 'ir.actions.act_url', 'url': draft_res,'target':'new',}
#                 redirect = werkzeug.utils.redirect(draft_res['_links']['draft:edit-form']['href'])
#                 redirect.autocorrect_location_header = False
                logging.info(draft_res)
                if draft_res['_links']:
                    if draft_res['_links'].get('draft:edit-form',None):
                        return draft_res['_links']['draft:edit-form']['href']
                    else:
                        return  draft_res['_links']['board:select-form']['href']
                
                else:
                    result="posting failed "
                
#                     job_post_res= post_job_to_boards(cr,uid,post_board_body,draft_res)
#                     if(job_post_res):
#                         result=job_post_res
#                     else:
#                         result="posting failed "
            else:
                result="posting failed "
        except Exception as e:
            logging.info(e)
            return "Unable to Process, Please try after some time"
        return result
def create_draft_job(self,cr,uid,draft_body):
    try:
        draft_url_obj='drafts'
        response,content=service_call(cr,uid,draft_url_obj,'POST',draft_body)
        logging.info(content)
        res_content = json.loads(content)
#         draft_id=res_content['id']
#         req_no = draft_body['requisition_number']
#         cr.execute("""select id from hr_recruitment_job where requisition_number = %s""",(req_no,) )
#         req_id=cr.fetchone()
#         job_model=self.pool.get('hr.recruitment.job')
#         job_model.write(cr, uid,req_id[0], {'draft_id' : draft_id}, context=None)
        logging.info(response['status'])  
        if response['status'] == '400' :
            logging.info(res_content['_links']['draft:edit-form']['href'])
            return res_content
        if  response['status'] == '201':
            return res_content
        elif response['status']=='401':
            return "Authentication Failed"
        if response['status'] not in return_codes:
            return "Unable to Process, Please try after some time"
    except Exception as e:
            logging.info(e)
            logging.info(traceback.format_exc())  
def save_board_data(self,cr,uid,requisition_number):
    try:
#         posting_url_obj='drafts/'+str(draft_id)+'/postings'
#         postings_body = boards_json
#         response,content=service_call(cr,uid,posting_url_obj,'POST',postings_body)
#         if  response['status'] == '202' :
#             return {
#                                   'code' : response['status'],
#                                   'message' : " Job Posted Successfully "
#                                   
#                                   }
#         elif response['status']=='401':
#             return "Authentication Failed"                       
#         if response['status'] not in return_codes:
#             return "Unable to Process, Please try after some time"
           job_val = get_job_id(cr, uid, requisition_number)
           logging.info(job_val)
           if isinstance(job_val, dict):
               board_val = get_job_boards_data(cr, uid, job_val['id']) 
               if isinstance(board_val, dict):
                   logging.info(board_val)
                   return board_val
               else:
                   return board_val
           else:
                return job_id
        
           
    except Exception as e:
            logging.info(e)
            logging.info(traceback.format_exc())
            return "Unable to Process, Please try after sometime"  
def update_job(self,cr,uid,data,board_data): 
   result=""
   try:
       if data and board_data:
           validate_obj = equest_validations.EquestValidations()
           if board_data:
               validate_result= validate_obj.validate(data,board_data['boards'])
           else :
               validate_result = "Please provide job or board data"
           if isinstance(validate_result, (bool)):
               data_map_obj = helper.EquestDataMap()
               job_map,board_map = data_map_obj.get_equest_job_map_data(data,board_data)
           else:
               return validate_result
       elif board_data:
           validate_obj = equest_validations.EquestValidations()
           if board_data:
               validate_result= validate_obj.validate(None,board_data['boards'])
           else :
               validate_result = "Please provide job or board data"
           if isinstance(validate_result, (bool)):
               data_map_obj = helper.EquestDataMap()
               board_map = data_map_obj.get_equest_job_map_data(None,board_data)          
           else:
               return validate_result
       else:
           return "please provide data or board_data"    
       requisition_number=board_map['requisition_number']
       if not board_data:
           return "please provide board data"
       method_type='POST'  
       if data:
           result=update_job_data_and_board_data(self,cr,uid,job_map,board_map['boards'])
           return result
       else:
           draft_id = 218153

     
#            cr.execute("""select draft_id from hr_recruitment_job where requisition_number = %s""",(requisition_number) )
#            draft_id=cr.fetchone()

           if draft_id:
             
               result=update_board_data(cr,uid,board_map['boards'],draft_id)
               if isinstance(result,dict):
                   return {
                                      'code' : result['code'] ,
                                      'message' : " Job updated Successfully "
                                      
                                      }
               else:
                    return result
           else :
               return "update failed"
   except Exception as e:
       logging.info(e)
       logging.info(traceback.format_exc())
       return "Unable to Process, Please try after sometime"    
   return result 
def update_job_data_and_board_data(self,cr,uid,post_body,post_board_body):
   try:  
       draft_id=create_draft_job(self,post_body)
       if(draft_id):
           update_response=post_job_to_boards(cr,uid,post_board_body,draft_id)
           if(update_response['code'] == '202'):
               result = update_response
           else:
               result="job update failed"
       else:
           result="job update failed"            
       return result
   except Exception as e:
       logging.info(e)
       logging.info(traceback.format_exc())
       return "Unable to Process, Please try after sometime"
def update_board_data(cr,uid,post_board_body,draft_id):
    try:    
        if(draft_id):
            update_response=post_job_to_boards(cr,uid,post_board_body,draft_id)
            logging.info(update_response)
            if(update_response['code'] == '202'):
               result = update_response
            else:
                result="job update failed"
        else:
            result="provide valid requisition_number"            
        return result
    except Exception as e:
        logging.info(e)
        logging.info(traceback.format_exc())
        return "Unable to Process, Please try after sometime"             
#delete_job_from_particular_board
def delete_job(self,cr,uid,job_data,board_data):
    try:
        board_ids=[]
        delete_board_ids=[]
        deleted_boards=[]   
        if board_data:
           validate_obj = equest_validations.EquestValidations()
           if board_data:
               validate_result= validate_obj.validate(None,board_data['boards'])
           else :
               validate_result = "Please provide board data"
           if isinstance(validate_result, (bool)):
               data_map_obj = helper.EquestDataMap()
               board_map = data_map_obj.get_equest_board_map_data(board_data)          
           else:
               return validate_result
        else:
            return "please provide board data"  
        if not board_data['requisition_number']:
            return "please provide requisition_number in board"
        requisition_number=board_data['requisition_number']    
        for board in board_data['boards']:
            board_ids.append(board['name'])
        if not board_ids:
            return "please provide board_ids"   
        job_val=get_job_id(cr,uid,requisition_number)        
        if isinstance(job_val, dict):
            delete_board_ids=get_job_board_details(cr,uid,job_val['id'],board_ids)               
            if type(delete_board_ids) not in[list]:
                logging.info('delete_board_ids is string')
                return delete_board_ids       
            deleted_boards=delete_boards(cr,uid,job_val['id'],delete_board_ids)
        else:
            return job_val
            
        if not deleted_boards:
           return "please provide valid board_ids"
        if deleted_boards:
           return {
                   'code' : '200',
                   'message' :"board deleted successfully"
                   
                   }
    except Exception as e:
        logging.info(e)
        logging.info(traceback.format_exc())
        
def close_requisition(self,cr,uid,requisition_number):
    try:
        job_val={}
        if requisition_number:
            job_val = get_job_id(cr,uid,requisition_number)
            delete_url =  'jobs/'+str(job_val['id'])
            job_response,job_content= service_call(cr,uid,delete_url,'DELETE',{})
            if  job_response['status'] == '204' :
                return {'code' : '204',
                        'message' : 'Requisition no:'+requisition_number+'deleted successfully'
                        }
            elif job_response['status']=='401':
                return "Authentication Failed"
            if job_response['status'] not in return_codes:
                return "Unable to Process, Please try after sometime" 
    except Exception as e:
        logging.info(e)
        logging.info(traceback.format_exc())
        raise osv.except_osv(_('Warning !'),_("Unable to Process, Please try after sometime"))   
def get_job_id(cr,uid,requisition_number):
    try:
        job_id_url =  'jobs?requisition_number='+str(requisition_number) 
        job_response,job_content= service_call(cr,uid,job_id_url,'GET',{})
        job_content = json.loads(job_content)
        
        
        if  job_response['status'] == '200':            
            logging.info(job_content)
            if(len(job_content)>0):
               return {
                       'id' : job_content[0]['id'] ,
                       'message' : "Job unique Id"
                }
            else:
                return "Please provide valid requisition number"
                
        elif job_response['status']=='401':
            return "Authentication Failed"
        if job_response['status'] not in return_codes:
            return "Unable to Process, Please try after sometime"
    except Exception as e:
        logging.info(e)
        logging.info(traceback.format_exc())
        raise osv.except_osv(_('Warning !'),_("Unable to Process, Please try after sometime")) 

def get_job_boards_data(cr,uid,job_id):
    try:
        delete_board_ids=[]
        posting_details_url =  'jobs/'+str(job_id)+'/postings'
        boards_response,boards_content= service_call(cr,uid,posting_details_url,'GET',{})
        boards_content = json.loads(boards_content)
        if boards_response['status'] == '200' :
#             for board_id in board_ids:
#                 for job_board in boards_content:
#                     if job_board['board']['id']==int(board_id):
#                         delete_board_ids.append({'job_board_id':job_board['id'],'board_id':board_id}) 
            return boards_content         
        elif boards_response['status']=='401':
            return "Authentication Failed"
        if boards_response['status'] not in return_codes:
            return "Unable to Process, Please try after sometime" 
    except Exception as e:
        logging.info(e)
        logging.info(traceback.format_exc())
        raise osv.except_osv(_('Warning !'),_("Unable to Process, Please try after sometime"))


def get_job_board_details(cr,uid,job_id,board_ids):
    try:
        delete_board_ids=[]
        posting_details_url =  'jobs/'+str(job_id)+'/postings'
        boards_response,boards_content= service_call(cr,uid,posting_details_url,'GET',{})
        boards_content = json.loads(boards_content)
        if boards_response['status'] == '200' :
            for board_id in board_ids:
                for job_board in boards_content:
                    if job_board['board']['name']==str(board_id):
                        delete_board_ids.append({'job_board_id':job_board['id'],'board_id':board_id}) 
            return delete_board_ids         
        elif boards_response['status']=='401':
            return "Authentication Failed"
        if boards_response['status'] not in return_codes:
            return "Unable to Process, Please try after sometime" 
    except Exception as e:
        logging.info(e)
        logging.info(traceback.format_exc())
        raise osv.except_osv(_('Warning !'),_("Unable to Process, Please try after sometime"))              
      
def delete_boards(cr,uid,job_id,delete_board_ids):    
    try:
        deleted_boards=[]
        for delete_board_id in delete_board_ids:                       
            delete_url ='jobs/'+str(job_id)+'/postings/'+str(delete_board_id['job_board_id'])
            delete_response,delete_content=service_call(cr,uid,delete_url,'DELETE',{})
            if  delete_response['status'] == '204' :
                
                deleted_boards.append(delete_board_id['board_id'])
            elif delete_response['status']=='401':
                return "Authentication Failed"
            if delete_response['status'] not in return_codes:
                raise osv.except_osv(_('Warning !'),_("Unable to Process, Please try after sometime")) 
        return deleted_boards
    except Exception as e:
        logging.info(e)
        logging.info(traceback.format_exc())
        raise osv.except_osv(_('Warning !'),_("Unable to Process, Please try after sometime"))
    
def get_boards(self,cr,uid):
    try:        
        get_board_url ='boards'
        board_response,board_content=service_call(cr,uid,get_board_url,'GET',{})
        if  board_response['status'] == '200' :
            return json.loads(board_content)
        elif board_response['status']=='401':
            return "Authentication Failed"
        elif board_response['status'] not in return_codes:
            raise osv.except_osv(_('Warning !'),_("Unable to Process, Please try after some time"))  
    except Exception as e:
        logging.info(e)
        logging.info(traceback.format_exc())
        raise osv.except_osv(_('Warning !'),_("Unable to Process, Please try after sometime"))
          

def service_call(cr,uid,url_obj,method_type,data_body):
    try:
        param_details = parameter_details(cr,uid)
        logging.info(param_details)
        if param_details:
            post_url_obj = param_details[0]['url']
            logging.info(post_url_obj)
            
            post_url_obj = str(post_url_obj)+str(url_obj)
            logging.info("------------------------")
            logging.info(post_url_obj)
            username = param_details[0]['user_name']
            password= param_details[0]['password']
            if username and password :
                auth = base64.encodestring( username + ':' + password)
            logging.info(auth)
            logging.info(url_obj)
            headers = {'Content-type': 'application/json', 'Authorization' : ' Basic  %s'  %  auth}
            json_request=json.dumps(data_body,cls=None)
            #http = httplib2.Http(proxy_info = httplib2.ProxyInfo(proxy_type=httplib2.socks.PROXY_TYPE_HTTP, proxy_host='172.16.6.61', proxy_port=8080,proxy_user = 'skrishna', proxy_pass = '123Welcome&'), disable_ssl_certificate_validation=True)
            
            http = httplib2.Http()  
            try:
                response, content = http.request(post_url_obj,method_type, headers=headers,  body=(json_request))
#                 logging.info(response)             
            except Exception as e:
                logging.info(e)
                raise osv.except_osv(_('Warning !'),_("Unable to Process, Please try after some time"))  
            return response,content
    except Exception as e:
            logging.info(e)
            logging.info(traceback.format_exc())
