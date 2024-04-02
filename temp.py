from mako.template import Template
from mako.lookup import TemplateLookup

hosts_file_path = '/tmp'
lookup = TemplateLookup(
    directories=[hosts_file_path],
    output_encoding='utf-8',
    input_encoding='utf-8',
    default_filters=['decode.utf8'],
    encoding_errors='replace'
)

hosts_file_tempalte = lookup.get_template("/hosts")
data = [{'hostname':'lithium11','ip':'172.16.100.110'},{'hostname':'lithium12','ip':'172.16.100.111'}]
# data = {'a':'234','b':'324'}
        # # for each_server in list_server_info:
        # #     ip_hostname_content = hosts_file_tempalte.render(
        # #         ip = list_server_info['ip'],
        # #         hostname = list_server_info['hostname']
        # #     )
                    
print(hosts_file_tempalte.render(data=data))