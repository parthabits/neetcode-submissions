class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        st = set()
        for email in emails:
            sp_email = email.split("@")
            localname, domain = sp_email[0], sp_email[1]
            localname = localname.replace('.', '')
            if '+' in localname:
                localname = localname.split('+')[0]
            st.add(localname + '@' + domain)
        return len(st)
            

        