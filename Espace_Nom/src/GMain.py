#================================================
import math as GMath
#================================================
from math import sqrt
from math import pow
#================================================
def namespace1():
    m_sqrt = GMath.sqrt(5)
    m_pow = GMath.pow(5, 2)
    m_format = ""

    m_format += "Namespace1 : m_sqrt : " + str(m_sqrt) + "\n"
    m_format += "Namespace1 : m_pow : " + str(m_pow) + "\n"

    print(m_format)
#================================================
def namespace2():
    m_sqrt = sqrt(5)
    m_pow = pow(5, 2)
    m_format = ""

    m_format += "Namespace2 : m_sqrt : " + str(m_sqrt) + "\n"
    m_format += "Namespace2 : m_pow : " + str(m_pow) + "\n"

    print(m_format)
#================================================
namespace1()
namespace2()
#================================================
