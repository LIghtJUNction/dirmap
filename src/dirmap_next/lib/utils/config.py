#!/usr/bin/env python3

'''
@Author: xxlin
@LastEditors: ttttmr
@Date: 2019-04-11 09:49:16
@LastEditTime: 2019-05-29 16:49:43
'''

from configparser import ConfigParser
from ..core.data import paths
from ..core.common import outputscreen


class ConfigFileParser:
    @staticmethod
    def _get_option(section: str, option: str) -> str:
        try:
            cf = ConfigParser()
            cf.read(paths.CONFIG_PATH)
            return cf.get(section=section, option=option)
        except:
            outputscreen.warning('Missing essential options, please check your config-file.')
            return ''


    def recursive_scan(self) -> str:
        return self._get_option('RecursiveScan','conf.recursive_scan')
    def recursive_status_code(self) -> str:
        return self._get_option('RecursiveScan','conf.recursive_status_code')
    def recursive_scan_max_url_length(self) -> str:
        return self._get_option('RecursiveScan','conf.recursive_scan_max_url_length')
    def recursive_blacklist_exts(self) -> str:
        return self._get_option('RecursiveScan','conf.recursive_blacklist_exts')
    def exclude_subdirs(self) -> str:
        return self._get_option('RecursiveScan','conf.exclude_subdirs')

    def dict_mode(self) -> str:
        return self._get_option('ScanModeHandler','conf.dict_mode')
    def dict_mode_load_single_dict(self) -> str:
        return self._get_option('ScanModeHandler','conf.dict_mode_load_single_dict')
    def dict_mode_load_mult_dict(self) -> str:
        return self._get_option('ScanModeHandler','conf.dict_mode_load_mult_dict')
    def blast_mode(self) -> str:
        return self._get_option('ScanModeHandler','conf.blast_mode')
    def blast_mode_min(self) -> str:
        return self._get_option('ScanModeHandler','conf.blast_mode_min')
    def blast_mode_max(self) -> str:
        return self._get_option('ScanModeHandler','conf.blast_mode_max')
    def blast_mode_az(self) -> str:
        return self._get_option('ScanModeHandler','conf.blast_mode_az')
    def blast_mode_num(self) -> str:
        return self._get_option('ScanModeHandler','conf.blast_mode_num')
    def blast_mode_custom_charset(self) -> str:
        return self._get_option('ScanModeHandler','conf.blast_mode_custom_charset')
    def blast_mode_resume_charset(self) -> str:
        return self._get_option('ScanModeHandler','conf.blast_mode_resume_charset')
    def crawl_mode(self) -> str:
        return self._get_option('ScanModeHandler','conf.crawl_mode')
    def crawl_mode_dynamic_fuzz_suffix(self) -> str:
        return self._get_option('ScanModeHandler','conf.crawl_mode_dynamic_fuzz_suffix')
    def crawl_mode_parse_robots(self) -> str:
        return self._get_option('ScanModeHandler','conf.crawl_mode_parse_robots')
    def crawl_mode_parse_html(self) -> str:
        return self._get_option('ScanModeHandler','conf.crawl_mode_parse_html')
    def crawl_mode_dynamic_fuzz(self) -> str:
        return self._get_option('ScanModeHandler','conf.crawl_mode_dynamic_fuzz')
    def fuzz_mode(self) -> str:
        return self._get_option('ScanModeHandler','conf.fuzz_mode')
    def fuzz_mode_load_single_dict(self) -> str:
        return self._get_option('ScanModeHandler','conf.fuzz_mode_load_single_dict')
    def fuzz_mode_load_mult_dict(self) -> str:
        return self._get_option('ScanModeHandler','conf.fuzz_mode_load_mult_dict')
    def fuzz_mode_label(self) -> str:
        return self._get_option('ScanModeHandler','conf.fuzz_mode_label')

    def request_headers(self) -> str:
        return self._get_option('RequestHandler','conf.request_headers')
    def request_header_ua(self) -> str:
        return self._get_option('RequestHandler','conf.request_header_ua')
    def request_header_cookie(self) -> str:
        return self._get_option('RequestHandler','conf.request_header_cookie')
    def request_header_401_auth(self) -> str:
        return self._get_option('RequestHandler','conf.request_header_401_auth')
    def request_timeout(self) -> str:
        return self._get_option('RequestHandler','conf.request_timeout')
    def request_delay(self) -> str:
        return self._get_option('RequestHandler','conf.request_delay')
    def request_limit(self) -> str:
        return self._get_option('RequestHandler','conf.request_limit')
    def request_max_retries(self) -> str:
        return self._get_option('RequestHandler','conf.request_max_retries')
    def request_persistent_connect(self) -> str:
        return self._get_option('RequestHandler','conf.request_persistent_connect')
    def request_method(self) -> str:
        return self._get_option('RequestHandler','conf.request_method')
    def redirection_302(self) -> str:
        return self._get_option('RequestHandler','conf.redirection_302')
    def file_extension(self) -> str:
        return self._get_option('RequestHandler','conf.file_extension')

    def response_status_code(self) -> str:
        return self._get_option('ResponseHandler','conf.response_status_code')
    def response_header_content_type(self) -> str:
        return self._get_option('ResponseHandler','conf.response_header_content_type')
    def response_size(self) -> str:
        return self._get_option('ResponseHandler','conf.response_size')
    def auto_check_404_page(self) -> str:
        return self._get_option('ResponseHandler','conf.auto_check_404_page')
    def custom_503_page(self) -> str:
        return self._get_option('ResponseHandler','conf.custom_503_page')
    def custom_response_page(self) -> str:
        return self._get_option('ResponseHandler','conf.custom_response_page')
    def skip_size(self) -> str:
        return self._get_option('ResponseHandler','conf.skip_size')

    def proxy_server(self) -> str:
        return self._get_option('ProxyHandler','conf.proxy_server')

    def debug(self) -> str:
        return self._get_option('DebugMode','conf.debug')
    def update(self) -> str:
        return self._get_option('CheckUpdate','conf.update')
