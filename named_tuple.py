Change = namedtuple('Change', ('old', 'new'))

auth_change = Change(invoice_line_item.authorized, data.get('authorized', None))
if auth_change.old != auth_change.new:
    if auth_change.new == True:
        invoice_line_item.authorize()
    else:
        invoice_line_item.deauthorize()
