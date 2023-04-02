# @Date   : 2022/9/23 17:31
# @Author : Andrew
# @Name   : guest
class Guest:
    def add_guest(self, sess, customerphone, customername, childsex, childdate,
                  creditkids, creditcloth):
        url_add_guest = 'http://192.168.4.32:8080/woniusales/customer/add'
        info = {
            "customername": f"{customername}",
            "customerphone": f"{customerphone}",
            "childsex": f"{childsex}",
            "childdate": f"{childdate}",
            "creditkids": f"{creditkids}",
            "creditcloth": f"{creditcloth}"
        }
        res_guest = sess.post(url_add_guest, data=info)
        return res_guest
