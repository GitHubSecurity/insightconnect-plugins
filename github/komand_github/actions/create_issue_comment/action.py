import komand
import github
from .schema import CreateCommentInput, CreateCommentOutput



class CreateIssueComment(komand.Action):
  def __init__(self):
      super(self.__class__, self).__init__(
              name='create_issue_comment',
              description='Create an issue comment',
              input=CreateCommentInput(),
              output=CreateCommentOutput())


  def run(self, params={}):
    if params.get('organization') and params.get('repository'):
      g = self.connection.github_user
      issue = g.get_organization(params.get('organization')).get_repo(params.get('repository')).get_issue(int(params.get('issue_number')))
    else:
      g = self.connection.user
      issue = g.get_repo(params.get('repository')).get_issue(int(params.get('issue_number')))

    issue_params = {"body": params.get("body")}

    issue = issue.create_comment(**issue_params)

    return {'url': issue.html_url}
