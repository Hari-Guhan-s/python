import job_posting_integrator
import logging
from openerp.osv import osv
import traceback

class JobBoardPostingApi():
    
    def traverse_job_board_api(self,cr,uid,action,tool_id,job_data,board_data):
        try:
            ats_integrator_obj = job_posting_integrator.JobPostingIntegrator()
            result = ats_integrator_obj.call_job_posting_api(cr,uid,action,tool_id,job_data,board_data)
            return result
        except Exception as e:
            logging.info(e)
            logging.info(traceback.format_exc())
        
        
        
    
    #- #def traverse_job_board_ats(self,uid,cr,method_name,job_data,board_data):
    #-------------------- def traverse_job_board_ats(self, job_data,board_data):
        #-------------------------------------------- if job_data or board_data:
            # #cr.execute('''select id from table name where name = condition ''')
            #----------------------------------------- #ats_name = cr.fetchone()
            #----------------------------------------------------- #if ats_name:
                #------------------------------------- #if ats_name == 'equest':
                    #------------------- #method_name = data.get('method',False)
                   #-------------------------------- # if method_name == 'post':
#------------------------------------------------------------------------------ 
            # #--------------------------------------- if job_data and board_data:
                # # validate_result= equest_data_map.validate_data(job_data, board_data)
# #------------------------------------------------------------------------------
            # #---------------------------------------------------- elif job_data:
                # # validate_result = equest_data_map.validate_data(job_data, None)
            # #-------------------------------------------------- elif board_data:
                # # validate_result= equest_data_map.validate_data(None, board_data)
            # #------------------------------------------------------------ else :
                # #---------- validate_result = "Please provide job or board data"
            # #--------------------------- if isinstance(validate_result, (bool)):
#------------------------------------------------------------------------------ 
            # #job_map,board_map = equest_data_map.get_equest_job_map_data(job_data,board_data)
            #------------- result  = equest_api.post_job(self,job_map,board_map)
            #-------------------------------------------------------- if result:
                #------------------------------------------------- return result
            #------------------------------------------------------------- else:
                #-------------------------------------------------- return False
        #----------------------------------------------------------------- else:
            #--------------------- return "please provide job and board details"
            # #if isinstance(job_map, (dict)) and isinstance(board_map, (dict)):
#------------------------------------------------------------------------------ 
                        # #------------------------------------------------- else:
                            # #-------------------------- return job_map,board_map
                    # #----------------------------- elif method_name == 'update':
                        # #------------------- equest_api.update(self,cr,uid,data)
                    # #----------------------------------------------------- else:
                        # # return self.error_response("Please enter valid post method")
            # #------------------------------------------------------------- else:
                # #----- return self.error_response("Please enter valid ats tool")
        # #----------------------------------------------------------------- else:
            # #------------- return self.error_response("Please enter valid data")
#------------------------------------------------------------------------------ 
#------------------------------------------------------------------------------ 
#------------------------------------------------------------------------------ 