import org.junit.jupiter.api.Test;
import org.python.Object;
import org.python.stdlib.datetime.DateTime;
import org.python.types.Bool;
import org.python.types.Int;
import org.python.types.Str;

import java.util.HashMap;
import java.util.Map;

import static org.junit.jupiter.api.Assertions.*;

public class DummyTest {

    @Test
    public void testSomething() {
        org.python.Object[] args = {null};

        Map<String, Object> kwargs = new HashMap<>();

        kwargs.put("year", Int.getInt(1997));
        kwargs.put("month", Int.getInt(11));
        kwargs.put("day", Int.getInt(7));
        kwargs.put("hour", Int.getInt(7));
        kwargs.put("minute", Int.getInt(34));
        kwargs.put("second", Int.getInt(19));
        kwargs.put("microsecond", Int.getInt(1997));

        DateTime mocked_date = new DateTime(args, kwargs);
        System.out.print(mocked_date);
        assertEquals(new Str("1997-11-07 07:34:19.001997"), mocked_date.__str__());
        assertEquals(new Str("1997"), mocked_date.year);
        assertEquals(new Str("11"), mocked_date.month);
        assertEquals(new Str("7"), mocked_date.day);
        assertEquals(new Str("7"), mocked_date.hour);
        assertEquals(new Str("34"), mocked_date.minute);
        assertEquals(new Str("19"), mocked_date.second);
        assertEquals(new Str("1997"), mocked_date.microsecond);
        assertNotEquals(new Str("199"), mocked_date.year);
        assertNotEquals(new Bool(true), mocked_date.year);
    }

}
