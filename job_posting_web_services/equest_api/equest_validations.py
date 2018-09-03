import logging

class EquestValidations():
    def validate(self,job_data=None,board_data=None):
        logging.info('job data')
        logging.info(job_data)
        if job_data:
#             if not job_data['requisition_number'] :
#                 return "Please enter valid requisition number"
#             elif not job_data['title']:
#                 return "Please enter valid title"
#             elif not job_data['description']:
#                 return "Please enter valid description"
#             elif not job_data['skills']:
#                 return "Please enter valid skills"
#             elif not job_data['country']:
#                 return "Please enter valid country"
#             elif not job_data['state']:
#                 return "Please enter valid state"
#             elif not job_data['city']:
#                 return "Please enter valid city"
#             elif not job_data['zip']:
#                 return "Please enter valid zip"
#             elif not job_data['function']:
#                 return "Please enter valid function"
#             elif not job_data['company_name']:
#                return "Please enter company name"
            if not job_data['account_email']:
                return "Please enter account email"
            elif not job_data['candidate_response_url']:
                return "Please enter candidate response url"
            elif not job_data['candidate_response_email']:
                return "Please enter candidate response email"
            elif not job_data['return_url']:
                return "Please enter candidate return url"
            else:
                return True
        if board_data:
            for data in board_data:
                if not data['name']:
                    return "Please enter valid board id"
                if not data['start_date']:
                    return "Please enter start_date"
            return True    