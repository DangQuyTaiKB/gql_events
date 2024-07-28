from uoishelpers.gqlpermissions import OnlyForAuthentized
from uoishelpers.gqlpermissions import MustBeOneOfPermission
OnlyForAdmins = MustBeOneOfPermission("administrátor")
from uoishelpers.gqlpermissions import RoleBasedPermission  
