import logging
import traceback


class EquestDataMap():

    def get_equest_job_map_data(self,job_data):
        try:
            job_map_data = {}
            board_map_data={}
            map_data={}
            if job_data:
                job_map_data={
                        "requisition_number":job_data['requisition_number'] if job_data.get('requisition_number',None) else "",
                
                        "position": {
                        "title": job_data['title'] if job_data.get('title',None) else "",
                        "description": job_data['description'] if job_data.get('description',None) else "",
                       "skills": job_data['skills'] if job_data.get('skills',None) else "",
                        "education": job_data['education'] if job_data.get('education',None) else "",
                        "benefits": job_data['benefits'] if job_data.get('benefits',None) else "",
                        "compensation": {
                            "range": {
                                "min": job_data['minsalary'] if job_data.get('minsalary',None) else "",
                                "max": job_data['maxsalary'] if job_data.get('maxsalary',None) else "",
                            },
                            "type":job_data['salarytype'] if job_data.get('salarytype',None) else "",
                            "currency": job_data['currency'] if job_data.get('currency',None) else "",
                        },
                        "location": {
                            "country": job_data['country'] if job_data.get('country',None) else "",
                            "state": job_data['state'] if job_data.get('state',None) else "",
                            "city": job_data['city'] if job_data.get('city',None) else "",
                            "zip": job_data['zip'] if job_data.get('zip',None) else ""
                        },
                        "travel_percentage": job_data['travel_percentage'] if job_data.get('travel_percentage',None) else "",
                        "telecommute_percentage":job_data['telecommute_percentage'] if job_data.get('telecommute_percentage',None) else "",
                        "classification": {
                            "type": job_data['employement_category'] if job_data.get('employement_category',None) else "",
                            "time": job_data['time'] if job_data.get('time',None) else "",
                            "function": job_data['function'] if job_data.get('function',None) else "",
                            "industry": job_data['industry'] if job_data.get('industry',None) else "",
                        }
                    },
                    "company": {
                        "name": job_data['company_name'] if job_data.get('company_name',None) else "",
                        "account": {
                            "name":job_data['account_name'] if job_data.get('account_name',None) else "",
                            "email": job_data['account_email'] if job_data.get('account_email',None) else "",
                            "organization": job_data['organization'] if job_data.get('organization',None) else "",
                        }
                    },
                    "candidate_response": {
                        "url": job_data['candidate_response_url'] if job_data.get('candidate_response_url',None) else "",
                        "email":job_data['candidate_response_email'] if job_data.get('candidate_response_email',None) else ""
                    },
                    "_links": {},
                    "return_url":job_data['return_url'] if job_data.get('return_url',None) else "",
                    } 
#             if board_data:
#                 board_map_data = self.get_equest_board_map_data(board_data)
#                 logging.info('board_map_data')
#                 logging.info(job_map_data) 
#                 logging.info(board_map_data) 
                #Eif board_map_data:
                    #map_data.update({'board_data':board_data_list})
            
            if job_map_data :      
                return job_map_data
#             elif board_map_data:
#                 return board_map_data
#             elif map_data:
#                 return job_map_data
            
            else:
                return None
                
        except Exception as e:
            logging.info(e)   
            logging.info(traceback.format_exc()) 
    def get_equest_board_map_data(self,board_data):
        try:
            if board_data:
                logging.info(board_data)
                board_data_list = []
                for values in board_data['boards']:
                    board_data_dict ={
                                      'board':{
                                               "id":values['id'] if values.get('id',None) else "",
                                               "bsd_required":True,
                                               "name":values['board_name'] if values.get('board_name',None) else ""
                                               },
                                      'board_status':{
                                                      "state":"queued",
                                                      "queued_at":values['start_date'] if values.get('start_date',None) else  ""
                                                      }
                                       }
                    board_data_list.append(board_data_dict)

                
                return {'requisition_number':board_data['requisition_number'],'boards':board_data_list}
            else:
                return None
        except Exception as e:
            logging.info(e)   
            logging.info(traceback.format_exc()) 
    

            
            
                           
        

