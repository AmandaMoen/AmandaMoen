# -*- coding: utf-8 -*-


def factorial(integer):
    """return the factorial of the provided integer"""
    if not isinstance(integer, int):
        raise ValueError("factorial requires integer input")

    if integer == 0:
        return 1

    return reduce(lambda x, y: x * y, range(integer, 0, -1))


if __name__ == '__main__':
    # code in here will __not__ be executed on import, but __will__ be run when
    # the file is executed from the command line
    vals = [
        (0, 1),
        (1, 1),
        (2, 2),
        (3, 6),
        (4, 24),
        (5, 120),
        (6, 720),
        (7, 5040),
        (8, 40320),
        (9, 362880),
        (10, 3628800),
        (11, 39916800),
        (12, 479001600),
        (13, 6227020800),
        (14, 87178291200),
        (15, 1307674368000),
        (16, 20922789888000),
        (17, 355687428096000),
        (18, 6402373705728000),
        (19, 121645100408832000),
        (20, 2432902008176640000),
        (21, 51090942171709440000),
        (22, 1124000727777607680000),
        (23, 25852016738884976640000),
        (24, 620448401733239439360000),
        (25, 15511210043330985984000000),
        (26, 403291461126605635584000000),
        (27, 10888869450418352160768000000),
        (28, 304888344611713860501504000000),
        (29, 8841761993739701954543616000000),
        (30, 265252859812191058636308480000000),
        (31, 8222838654177922817725562880000000),
        (32, 263130836933693530167218012160000000),
        (33, 8683317618811886495518194401280000000),
        (34, 295232799039604140847618609643520000000),
        (35, 10333147966386144929666651337523200000000),
        (36, 371993326789901217467999448150835200000000),
        (37, 13763753091226345046315979581580902400000000),
        (38, 523022617466601111760007224100074291200000000),
        (39, 20397882081197443358640281739902897356800000000),
        (40, 815915283247897734345611269596115894272000000000),
        (41, 33452526613163807108170062053440751665152000000000),
        (42, 1405006117752879898543142606244511569936384000000000),
        (43, 60415263063373835637355132068513997507264512000000000),
        (44, 2658271574788448768043625811014615890319638528000000000),
        (45, 119622220865480194561963161495657715064383733760000000000),
        (46, 5502622159812088949850305428800254892961651752960000000000),
        (47, 258623241511168180642964355153611979969197632389120000000000),
        (48, 12413915592536072670862289047373375038521486354677760000000000),
        (49, 608281864034267560872252163321295376887552831379210240000000000),
        (50, 30414093201713378043612608166064768844377641568960512000000000000),
    ]

    for input, output in vals:
        assert factorial(input) == output

    for badval in [3.5, 'a', [2,3,4]]:
        try:
            result = factorial(badval)
        except ValueError:
            pass
        else:
            print u"a bad value did not raise the expected error"
            assert(False)

    print "All tests pass"
