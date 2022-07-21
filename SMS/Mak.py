# Mak MOdule

from Admin import Service           # Admin is a Package
Service.admin_service()             # Service is a Module and admin_service is a method
print()
from Admin import Product           # Admin is a Package
Product.admin_product()             # Product is a Module and admin_product is a method
print()
from Admin.Common import Header     # Admin.Common is a Package and Header is a Module
Header.admin_common_header()        # Header is a Module and admin_common_header is a method
print()
from Admin.Common import Footer     #Admin.Common is a Package and Footer is a Module
Footer.admin_common_footer()        # Footer is a Module and admin_common_footer is a method
print()
from Users import Profile           # Users is a Package and Profile is a Module
Profile.user_profile()              # Profile is Module and user_profile is a method
print()
from Users import Request           # Users is a Package and Request is a Module
Request.user_request()              # Request is Module and user_request is a method