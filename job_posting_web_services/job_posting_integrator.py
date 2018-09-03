from equest_api import equest_api
from equest_api  import helper
import logging
import traceback

class JobPostingIntegrator():
    
   def call_job_posting_api(self,cr,uid,action,tool_id,job_data,board_data):
       try:
            #cr.execute('''select id from table name where name = condition ''')
            #----------------------------------------- #tool_name = cr.fetchone()
           tool_name ='equest'
           if tool_name:
               if tool_name == 'equest':
                   if action == 'post_job':
                       result  = equest_api.post_job(self,cr,uid,job_data)
                       if result:
                           return result
                       else:
                           return "Invalid request"
                        
                   elif action == 'update_job_post':
                       result  = equest_api.update_job(self,cr,uid,job_data,board_data)
                       if result:
                           return result
                       else:
                           return "Invalid request"
                   elif action == 'save_boards':
                       result  = equest_api.save_board_data(self,cr,uid,job_data)
                       if result:
                           return result
                       else:
                           return "Invalid request"
                        
                   elif action == 'delete_job_post':
                       result  = equest_api.delete_job(self,cr,uid,None,board_data) 
                       if result:
                           return result
                       else:
                           return "Invalid request"
                      
                   elif action == 'delete_job':
                       result  = equest_api.close_requisition(self,cr,uid,job_data) 
                       if result:
                           return result
                       else:
                           return "Invalid request"
                   elif action == 'get_boards':
                       result  = equest_api.get_boards(self,cr,uid) 
                       if result:
                           return result
                       else:
                           return "Invalid request"
                   else:
                       return "Please pass valid action"
           else:
               return "Please pass valid tool ID"
       except Exception as e:
           logging.info(e)
           logging.info(traceback.format_exc() )