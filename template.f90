!
! Template fortran module
!

module template

  implicit none
  private
  public :: foo
  public :: bar
  implicit none

contains

  function foo(a) result(b)

    implicit none
    real(8), intent(in) :: a
    real(8)             :: b

  end function foo


  subroutine bar(c, d)

    implicit none
    real(8), intent(in)  :: c
    real(8), intent(out) :: d

  end subroutine bar


end module template