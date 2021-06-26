"""
Generate template
"""

import sys
import os


def template_module(module="template", extension="f90", temp_function=True, temp_subroutine=True):
    """Get template for fortran file
    
    Args:
        module (str): name of module
        extension (str): extension, e.g. "f90"
    """
    # get file path
    filepath = f"./{module}.{extension}"
    with open(filepath, "w+") as f:
        # initialize template module
        f.write(f"!\n! Template fortran module\n!\n\n")
        f.write(f"module {module}\n\n")
        f.write(f"  implicit none\n")
        f.write(f"  private\n")
        if temp_function==True:
            f.write(f"  public :: foo\n")
        if temp_subroutine==True:
            f.write(f"  public :: bar\n")
        f.write(f"  implicit none\n\n")

        f.write(f"contains\n\n")

        # include template subroutine
        if temp_function==True:
            f.write(f"  function foo(a) result(b)\n\n")
            f.write(f"    implicit none\n")
            f.write(f"    real(8), intent(in) :: a\n")
            f.write(f"    real(8)             :: b\n\n")
            f.write(f"  end function foo\n\n\n")

        # include template function
        if temp_subroutine==True:
            f.write(f"  subroutine bar(c, d)\n\n")
            f.write(f"    implicit none\n")
            f.write(f"    real(8), intent(in)  :: c\n")
            f.write(f"    real(8), intent(out) :: d\n\n")
            f.write(f"  end subroutine bar\n\n\n")

        # end module
        f.write(f"end module {module}")
    print(f"Created {filepath}!")
    return


if __name__=="__main__":
    if len(sys.argv) > 1:
        module_name = sys.argv[1]
    else:
        module_name = "template"
    template_module(module=module_name)