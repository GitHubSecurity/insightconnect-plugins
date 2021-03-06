from komand.exceptions import ConnectionTestException
import xmltodict
import requests
import json
from komand.connection import Connection


class Request(object):
    def __init__(self, logger, url, session, key, verify_cert):
        self.logger = logger
        self.url = url
        self.session = session
        self.key = key
        self.verify_cert = verify_cert

    @classmethod
    def new_session(cls, connection: Connection, username: str, password: str, hostname: str, verify_cert: bool):
        url = hostname + "/api/"
        querystring = {"type": "keygen", "user": username, "password": password}

        try:
            session = requests.session()
            token_response = session.get(url, params=querystring, verify=verify_cert)
            token_dict = xmltodict.parse(token_response.text)
            try:
                pan_os_key = token_dict["response"]["result"]["key"]
                connection.logger.info("Key obtained")
            except KeyError:
                raise ConnectionTestException(
                    preset=ConnectionTestException.Preset.USERNAME_PASSWORD)

        except BaseException as e:
            raise Exception("Could not authenticate with PAN-OS: " + str(e))
        return cls(logger=connection.logger, url=url, session=session, key=pan_os_key,
                   verify_cert=verify_cert)

    def edit_(self, xpath: str, element: str) -> dict:
        """
        Overwrites The current element found at the xpath with the new element
        :param xpath: a syntax for selecting nodes from within an XML document
        :param element: information on a object in XML format
        :return Response from PAN-OS
        """

        querystring = {"type": "config", "action": "edit", "key": self.key, "xpath": xpath,
                       "element": element}
        try:
            response = self.session.post(self.url, params=querystring, verify=self.verify_cert)
            output = xmltodict.parse(response.text)
        except BaseException as e:
            self.logger.error("Could not edit specified PAN-OS config object. Error: " + str(e))
            raise
        if output['response']['@status'] == 'error':
            error = output['response']['msg']
            error = json.dumps(error)
            self.logger.error(
                'Palo Alto PAN-OS returned an error in response to the request: {}'.format(error))
            raise Exception('Palo Alto PAN-OS error')
        return {"response": output}

    def delete_(self, xpath: str) -> dict:
        """
        Deletes the element at the xpath
        :param xpath: a syntax for selecting nodes from within an XML document
        :return Response from PAN-OS
        """

        querystring = {"type": "config", "action": "delete", "key": self.key, "xpath": xpath}
        try:
            response = self.session.get(self.url, params=querystring, verify=self.verify_cert)
            output = xmltodict.parse(response.text)
        except BaseException as e:
            self.logger.error("Could not create specified PAN-OS config object"
                              " at the specified location. Error: " + str(e))
            raise
        if output['response']['@status'] == 'error':
            error = output['response']['msg']
            error = json.dumps(error)
            self.logger.error(
                'Palo Alto PAN-OS returned an error in response to the request: {}'.format(error))
            raise Exception('Palo Alto PAN-OS error')
        return output

    def get_(self, xpath: str) -> dict:
        """
        Returns the element at the xpath
        :param xpath: syntax for selecting nodes from within an XML document
        :return Response from PAN-OS
        """

        querystring = {"type": "config", "action": "get", "key": self.key, "xpath": xpath}
        try:
            response = self.session.get(self.url, params=querystring, verify=self.verify_cert)
            output = xmltodict.parse(response.text)
        except BaseException as e:
            self.logger.error("Could not create specified PAN-OS config object"
                              " at the specified location. Error: " + str(e))
            raise
        if output['response']['@status'] == 'error':
            error = output['response']['msg']
            error = json.dumps(error)
            self.logger.error(
                'Palo Alto PAN-OS returned an error in response to the request: {}'.format(error))
            raise Exception('Palo Alto PAN-OS error')
        return output

    def set_(self, xpath: str, element: str) -> dict:
        """
        Creates a new element at the xpath
        :param xpath: a syntax for selecting nodes from within an XML document
        :param element: information on a object in XML format
        :return Response from PAN-OS
        """

        querystring = {"type": "config", "action": "set", "key": self.key, "xpath": xpath,
                       "element": element}
        try:
            response = self.session.post(self.url, params=querystring, verify=self.verify_cert)
            output = xmltodict.parse(response.text)
        except BaseException as e:
            self.logger.error("Could not create specified PAN-OS config object"
                              " at the specified location. Error: " + str(e))
            raise
        if output['response']['@status'] == 'error':
            error = output['response']['msg']
            error = json.dumps(error)
            self.logger.error(
                'Palo Alto PAN-OS returned an error in response to the request: {}'.format(error))
            raise Exception('Palo Alto PAN-OS error')
        return output

    def show_(self, xpath: str) -> dict:
        """
        Returns the element at the xpath
        :param xpath: a syntax for selecting nodes from within an XML document
        :return Response from PAN-OS
        """

        querystring = {"type": "config", "action": "show", "key": self.key, "xpath": xpath}
        try:
            response = self.session.get(self.url, params=querystring, verify=self.verify_cert)
            output = xmltodict.parse(response.text)
        except BaseException as e:
            self.logger.error("Could not create specified PAN-OS config object"
                              " at the specified location. Error: " + str(e))
            raise
        if output['response']['@status'] == 'error':
            error = output['response']['msg']
            error = json.dumps(error)
            self.logger.error(
                'Palo Alto PAN-OS returned an error in response to the request: {}'.format(error))
            raise Exception('Palo Alto PAN-OS error')
        return output

    def op(self, cmd: str)-> dict:
        querystring = {"type": "op", "key": self.key, "cmd": cmd}
        try:
            response = self.session.get(self.url, params=querystring, verify=self.verify_cert)
            output = xmltodict.parse(response.text)
        except BaseException as e:
            self.logger.error("Could not create specified PAN-OS config object"
                              " at the specified location. Error: " + str(e))
            raise
        if output['response']['@status'] == 'error':
            error = output['response']['msg']
            error = json.dumps(error)
            self.logger.error(
                'Palo Alto PAN-OS returned an error in response to the request: {}'.format(error))
            raise Exception('Palo Alto PAN-OS error')
        return output

    def commit(self, action: str, cmd: str)-> dict:
        querystring = {"type": "commit", "action": action,
                       "key": self.key, "cmd": cmd}
        try:
            response = requests.get(self.url,
                                    params=querystring, verify=self.verify_cert)
            output = xmltodict.parse(response.text)
        except BaseException as e:
            self.logger.error("Could not commit candidate configuration. Error: " + str(e))
            raise

        if output['response']['@status'] == 'error':
            error = output['response']['msg']
            error = json.dumps(error)
            self.logger.error(
                'Palo Alto PAN-OS returned an error in response to the request: {}'.format(error))
            raise Exception('Palo Alto PAN-OS error')
        return output
